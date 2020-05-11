import os
import sys
import re
import numpy as np
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Scorer import Scorer

def convert_harm(user_out):
    "初期設定のuserの出力を変換する関数"
    return round(float(user_out.decode("utf-8")),3)


def main():
    S_basic = Scorer(os.getcwd())
    
    S_basic.test_stdout("HarmonicMean",convert=convert_harm,testdata = 79.902, max_score=10)
    
    
    S_basic.test_function("Triangle", "compute", 
                    testdata_in=[5,12,13], testdata_out=0, max_score=10)
    
    
    S_applied = Scorer(os.getcwd())
    S_applied.test_function("QuadEquation", "QuadEquation",
                    testdata_in=[0, 1, -2], testdata_out=2, max_score=2)
    
    S_applied.test_function("QuadEquation", "QuadEquation",convert=lambda x: (min(x),max(x)),
                    testdata_in=[1, -7, 12], testdata_out=(3, 4), max_score=2)
    
    S_applied.test_function("QuadEquation", "QuadEquation",convert=lambda x: (min(x),max(x)),
                    testdata_in=[1, 1, -2], testdata_out=(-2, 1), max_score=2)
    
    S_applied.test_function("QuadEquation", "QuadEquation",
                    testdata_in=[3, 1, 8], testdata_out="no solutions", max_score=2)
    
    S_applied.test_function("QuadEquation", "QuadEquation",
                    testdata_in=[2, 8, 8], testdata_out= -2, max_score=2)
    
    df_basic = pd.DataFrame({"ID":list(S_basic.score_dict.keys()),"通常":list(S_basic.score_dict.values())})
    df_applied = pd.DataFrame({"ID":list(S_applied.score_dict.keys()),"応用":list(S_applied.score_dict.values())})
                            
    df_score = pd.merge(df_basic,df_applied,on="ID", how="outer").fillna(0)
    df_score.sort_values("ID")
    df_score.to_csv("score.csv",index=False)
    
if __name__ == "__main__":
    main()
