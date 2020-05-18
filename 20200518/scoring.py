import os
import sys
import re
import numpy as np
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Scorer import Scorer

def convert_density(user_out):
    "初期設定のuserの出力を変換する関数"
    out = user_out.decode("utf-8")
    p = re.compile("[+-]?\d+(?:\.\d+)?")
    match_list = p.findall(out)
    match_list = [round(float(i),3) for i in match_list]
    match_list.sort()
    return match_list

def convert_montecarlo(user_out):
    "初期設定のuserの出力を変換する関数"
    out = user_out.decode("utf-8")
    p = re.compile("[+-]?\d+(?:\.\d+)?")
    match_list = p.findall(out)
    estimated_pi = max([float(i) for i in match_list])
    return estimated_pi > 3.1 and estimated_pi < 3.2

testdata_density = [1.105, 5.957, 6.904, 10.232, 10.956, 17.15, 19.291, 24.157, 25.234, 34.169, 35.173, 37.544, 39.948, 50.612, 54.918, 55.088, 55.649, 58.133, 61.761, 62.349, 65.165, 76.529, 86.39, 87.68, 88.309, 92.211, 97.778, 98.468, 102.318, 108.773, 128.435, 141.562, 149.121, 154.138, 168.148, 180.42, 182.985, 193.113, 222.436, 234.17, 258.127, 277.366, 297.346, 360.208, 371.936, 477.899, 634.15, 648.761, 680.59, 1020.215]

def main():
    S_basic = Scorer(os.getcwd())
    
    print("##### Density #####")
    S_basic.test_stdout("Density",convert=convert_density,testdata = testdata_density, max_score=10)
    
    print("##### MonteCarlo #####")
    S_basic.test_stdout("MonteCarlo",convert=convert_montecarlo,testdata = True, max_score=10)
    
    S_applied = Scorer(os.getcwd())
    print("##### PrimeFactorization 1 #####")
    S_applied.test_function("PrimeFactorization", "PrimeFactorization",
                    testdata_in=[12], testdata_out=[[2,2],[3,1]], max_score=2)
    
    print("##### PrimeFactorization 2 #####")
    S_applied.test_function("PrimeFactorization", "PrimeFactorization",
                    testdata_in=[30], testdata_out=[[2,1],[3,1],[5,1]], max_score=2)
    
    print("##### PrimeFactorization 3 #####")
    S_applied.test_function("PrimeFactorization", "PrimeFactorization",
                    testdata_in= [32], testdata_out=[[2,5]], max_score=2)
    
    print("##### PrimeFactorization 4 #####")
    S_applied.test_function("PrimeFactorization", "PrimeFactorization",
                    testdata_in= [111], testdata_out=[[3, 1], [37, 1]], max_score=2)
    
    print("##### PrimeFactorization 5 #####")
    S_applied.test_function("PrimeFactorization", "PrimeFactorization",
                    testdata_in= [20200518], testdata_out=[[2, 1], [3, 2], [13, 1], [173, 1], [499, 1]], max_score=2)
    
    
    df_basic = pd.DataFrame({"ID":list(S_basic.score_dict.keys()),"通常":list(S_basic.score_dict.values())})
    df_applied = pd.DataFrame({"ID":list(S_applied.score_dict.keys()),"応用":list(S_applied.score_dict.values())})
                            
    df_score = pd.merge(df_basic,df_applied,on="ID", how="outer").fillna(0)
    df_score.sort_values("ID")
    df_score.to_csv("score.csv",index=False)
    
if __name__ == "__main__":
    main()
