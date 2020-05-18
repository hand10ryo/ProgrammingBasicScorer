import os
import sys
import re
import numpy as np
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Scorer import Scorer

def convert_harm(user_out):
    "初期設定のuserの出力を変換する関数"
    out = user_out.decode("utf-8")
    p = re.compile("[+-]?\d+(?:\.\d+)?")
    match_list = p.findall(out)
    return round(float(match_list[0]),3)

def convert_tri(user_out):
    "初期設定のuserの出力を変換する関数"
    out = user_out.decode("utf-8")
    p = re.compile("[+-]?\d+(?:\.\d+)?")
    match_list = p.findall(out)
    return max([float(i) for i in match_list])


def main():
    S_basic = Scorer(os.getcwd())
    
    print("##### Harmonic Mean #####")
    S_basic.test_stdout("HarmonicMean",convert=convert_harm,testdata = 79.902, max_score=10)
    
    print("##### Triangle 1 #####")
    S_basic.test_stdout("Triangle",convert=convert_tri,testdata = 6, max_score=3, stdin_file="triangle_stdin1.py")
    
    print("##### Triangle 2 #####")
    S_basic.test_stdout("Triangle",convert=convert_tri,testdata = 30, max_score=4, stdin_file="triangle_stdin2.py")
    
    print("##### Triangle 3 #####")
    S_basic.test_stdout("Triangle",convert=convert_tri,testdata = 60, max_score=4, stdin_file="triangle_stdin3.py")
    
    
    S_applied = Scorer(os.getcwd())
    print("##### QuadEquation 1 #####")
    S_applied.test_function("QuadEquation", "QuadEquation",
                    testdata_in=[0, 1, -2], testdata_out=2, max_score=2)
    
    print("##### QuadEquation 2 #####")
    S_applied.test_function("QuadEquation", "QuadEquation",convert=lambda x: (min(x),max(x)),
                    testdata_in=[1, -7, 12], testdata_out=(3, 4), max_score=2)
    
    print("##### QuadEquation 3 #####")
    S_applied.test_function("QuadEquation", "QuadEquation",convert=lambda x: (min(x),max(x)),
                    testdata_in=[1, 1, -2], testdata_out=(-2, 1), max_score=2)
    
    print("##### QuadEquation 4 #####")
    S_applied.test_function("QuadEquation", "QuadEquation",
                    testdata_in=[3, 1, 8], testdata_out="no solutions", max_score=2)
    
    print("##### QuadEquation 5 #####")
    S_applied.test_function("QuadEquation", "QuadEquation",
                    testdata_in=[2, 8, 8], testdata_out= -2, max_score=2)
    
    df_basic = pd.DataFrame({"ID":list(S_basic.score_dict.keys()),"通常":list(S_basic.score_dict.values())})
    df_applied = pd.DataFrame({"ID":list(S_applied.score_dict.keys()),"応用":list(S_applied.score_dict.values())})
                            
    df_score = pd.merge(df_basic,df_applied,on="ID", how="outer").fillna(0)
    df_score.sort_values("ID")
    df_score.to_csv("score.csv",index=False)
    
if __name__ == "__main__":
    main()
