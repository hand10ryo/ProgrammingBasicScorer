import os
import sys
import glob
import subprocess
import importlib

def convert(user_out):
    "初期設定のuserの出力を変換する関数"
    return user_out.decode("utf-8")

def load_data(path, filename):
    "初期設定のテストデータを読み込む関数"
    data_path = path + "/" + filename + "_test.txt"
    with open(data_path, "r") as f:
        data = f.read()
    return data
           
class Scorer:
    "スコア付けをするクラス"
    def __init__(self, path):
        self.path = path
        self.test_dir = path + "/submit"
        self.score_dict = {}
        
    def test_stdout(self, filename, convert=convert, testdata = None, max_score=1):
        """"
        課題が標準出力のときに使う関数
        
        - input
        filename : 【文字列】〜.pyの~を文字列で
        convert：【関数】上のconvert関数が初期設定。ユーザーの出力を弄りたければこれを設定
        testdata：【関数】 初期設定では上のload_dataでtestdataを読み込むが、文字列以外のデータを使いたければこれを設定する。
        max_score：【float】最大点
        
        - output
        None
        
        """
        test_file_list = glob.glob(self.test_dir+ "/*" + filename + ".py")
        for test_file in test_file_list:
            ID = test_file.split("/")[-1][:8]
            try:
                proc = subprocess.Popen(
                    ['python', test_file], 
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                out, err = proc.communicate()
                out_conv = convert(out)
                err = err.decode("utf-8")
            except:
                out = ""
                out_conv = ""
                err = "maybe timeout"
            
            if testdata is None:
                testdata = load_data(self.path, filename)
                
            if out_conv == testdata:
                print(ID, "OK")
                score = 1
            else:
                print("###########  code  ###############")
                with open(test_file, "r") as f:
                    print(f.read())
                print("###########  output ###############")
                print(out_conv)
                print("###########  error ###############")
                print(err)
                print()
                print(f"{ID}'s code is something wrong. Input partial score in [0,1]")
                score = float(input())

            if ID in self.score_dict.keys():
                self.score_dict[ID] += score * max_score
            else:
                self.score_dict[ID] = score * max_score
                
    def test_function(self, filename, funcname, convert=lambda x:x, 
                      testdata_in = [], testdata_out=None, max_score=1):
        """"
        課題が関数のときに使う関数
        
        - input
        filename : 【文字列】〜.pyの~を文字列で
        funcname：【文字列課題の対象となる関数の名前
        convert：【関数】恒等写像が初期設定。ユーザーの出力を弄りたければこれを設定
        testdata_in：【リスト】対象の関数に入力する引数をリストで 
        testdata_out：【オブジェクト】対象の関数の返り値をconvert関数に入力したときの想定する出力をオブジェクトで。
        　　　　　　　　　ただし"=="で正誤判定することに注意
        max_score：【float】最大点
        
        - output
        None
        
        """

        test_file_list = glob.glob(self.test_dir+ "/*" + filename + ".py")
        sys.path.append(self.test_dir)
        for test_file in test_file_list:
            pyfile = test_file.split("/")[-1][:-3]
            ID = pyfile[:8]
            
            try:
                mod = importlib.import_module(pyfile, package=None)
                func = getattr(mod, funcname)
                user_out = func(*testdata_in)
                out = convert(user_out)
            except:
                out = None
            
            if out == testdata_out:
                print(ID, "OK")
                score = 1
            else:
                print("###########  code  ###############")
                with open(test_file, "r") as f:
                    print(f.read())
                print("###########  output ###############")
                print(out)
                #print("###########  error ###############")
                #print(err)
                print()
                print(f"{ID}'s code is something wrong. Input partial score in [0,1]")
                score = float(input())
            
            if ID in self.score_dict.keys():
                self.score_dict[ID] += score * max_score
            else:
                self.score_dict[ID] = score * max_score
        