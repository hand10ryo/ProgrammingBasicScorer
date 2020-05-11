import os
import glob
import itertools

import Levenshtein
import pandas as pd


def similarity_cal(code_str1,code_str2):
    #delete indent tab space zenkakuspace kaigyou
    table = str.maketrans({
        '\u3000': '',
        ' ': '',
        '\t': '',
        '\n':''})
    string1 = code_str1.translate(table)
    string2 = code_str2.translate(table)
    distance=Levenshtein.distance(string1, string2)
    text_len=(len(string1)+len(string2))/2
    return 1 - distance/text_len

#類似度ランキング
def copy_checker(path):
    """copycheckを行う関数
    
    - input
    path:【文字列】ワイルドカードを使って該当するチェックしたいファイルを全て指定する
    
    - output
    
    """
    py_list = glob.glob(path)
    #similarity_comb　=　[]
    df_similarity = pd.DataFrame({"file1":[],"file2":[],"similarity":[]})
    file_comb=list(itertools.combinations(py_list,2))
    for first_file,second_file in file_comb:
        with open(first_file) as f:
            string1 = f.read()
        with open(second_file) as f:
            string2 = f.read()

        similaty=similarity_cal(code_str1=string1,code_str2=string2)
        
        df_similarity_line = pd.DataFrame({"file1":[first_file],
                                           "file2":[second_file],
                                           "similarity":[similaty]})
        
        df_similarity = pd.concat([df_similarity, df_similarity_line])
        #similarity_comb.append([similaty,[first_file,second_file]])
        
    return df_similarity.sort_values("similarity",ascending=False)


def get_ID(x):
    year = int(x.split("/")[-1][:2])
    idx = int(x.split("/")[-1][3:8])
    return year*100000 + idx

def get_df_with_ID(df,test=True):
    df_copy = df.copy()
    df_copy["ID1"] = df_copy["file1"].map(get_ID)
    df_copy["ID2"] = df_copy["file2"].map(get_ID)
    df_copy["ID_min"] = df_copy[["ID1","ID2"]].apply(lambda x:min(x),axis=1)
    df_copy["ID_max"] = df_copy[["ID1","ID2"]].apply(lambda x:max(x),axis=1)
    return df_copy

def copy_checker_by_filename(filename, test=False):
    if test:
        path = os.getcwd() + f"/testsubmit/*{filename}.py"
    else:
        path = os.getcwd() + f"/submit/*{filename}.py"
    df = copy_checker(path)
    df = get_df_with_ID(df)
    return df.pivot(index="ID_min",columns="ID_max",values="similarity")
    