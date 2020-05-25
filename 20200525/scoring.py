import os
import sys
import re
import numpy as np
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Scorer import Scorer

def convert_Matrix(user_out):
    out = user_out.decode("utf-8")
    p = re.compile("[+-]?\d+(?:\.\d+)?")
    match_list = p.findall(out)
    return [round(float(i)) for i in match_list]

def convert_Power20(user_out):
    out = user_out.decode("utf-8")
    p = re.compile("[+-]?\d+(?:\.\d+)?")
    match_list = p.findall(out)
    return [round(float(i)) for i in match_list]

def convert_Power20_2(user_out):
    out = np.array(user_out).round(3).tolist()
    return out


def main():
    S_basic = Scorer(os.getcwd())
    
    # MatrixMatrixの課題
    testdata_matrix = [30, 30, 45, 75, 58, 80, 75, 62, 85]
    S_basic.test_stdout("MatrixMatrix",convert = convert_Matrix,testdata=testdata_matrix, max_score=10)

    # Power20の標準出力の課題
    S_applied = Scorer(os.getcwd())
    testdata_pow = [68586, 34420,75432,63894,37660,18901,41423,35087,70324,35307,77377,65538,105001,52701,115496,97829]
    
    S_applied.test_stdout("Power20",convert = convert_Power20, testdata=testdata_pow, max_score=5)
    
    # Power20の関数の課題
    testdata_in = [[[0.1, 0.2, 0.3, 0.4],
                    [0.5, 0.6, 0.7, 0.8],
                    [0.9, 0.10, 0.11, 0.12],
                    [0.13, 0.14, 0.15, 0.16]]]
    
    testdata_out = [[17.947, 11.41 , 14.022, 16.633],
                    [49.864, 31.703, 38.959, 46.214],
                    [19.887, 12.644, 15.537, 18.431],
                    [11.37 ,  7.229,  8.883, 10.538]]
    
    S_applied.test_function("Power20", "Power20", convert = convert_Power20_2,
                    testdata_in=testdata_in, testdata_out=testdata_out, max_score=5)
    
    df_basic = pd.DataFrame({"ID":list(S_basic.score_dict.keys()),"通常":list(S_basic.score_dict.values())})
    df_applied = pd.DataFrame({"ID":list(S_applied.score_dict.keys()),"応用":list(S_applied.score_dict.values())})
                            
    df_score = pd.merge(df_basic,df_applied,on="ID", how="outer").fillna(0)
    df_score.sort_values("ID")
    df_score.to_csv("score.csv",index=False)
    
if __name__ == "__main__":
    main()
