import os
import sys
import re
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Scorer import Scorer

def convert_Power20(user_out):
    out = user_out.decode("utf-8")
    p = re.compile('[0-9]{6}\.[0-9]{3}')
    match_list = p.findall(out)
    return [round(float(i)) for i in match_list]

def convert_Power20_2(user_out):
    out = np.array(user_out).round(3).tolist()
    return out


def main():
    S = Scorer(os.getcwd())
    
    # MatrixMatrixの課題
    S.test_stdout("MatrixMatrix")

    # Power20の標準出力の課題
    testdata = [205485., 205485., 205485., 205484.,
                247793., 247789., 247792., 247788.,
                269950., 269950., 269949., 269952.,
                325348., 325352., 325350., 325351.]
    
    S.test_stdout("Power20",convert = convert_Power20, testdata=testdata, max_score=0.5)
    
    # Power20の関数の課題
    testdata_in = [[[0.1, 0.2, 0.3, 0.4],
                    [0.5, 0.6, 0.7, 0.8],
                    [0.9, 0.10, 0.11, 0.12],
                    [0.13, 0.14, 0.15, 0.16]]]
    
    testdata_out = [[17.947, 11.41 , 14.022, 16.633],
                    [49.864, 31.703, 38.959, 46.214],
                    [19.887, 12.644, 15.537, 18.431],
                    [11.37 ,  7.229,  8.883, 10.538]]
    
    S.test_function("Power20", "Power20", convert = convert_Power20_2,
                    testdata_in=testdata_in, testdata_out=testdata_out, max_score=0.5)
    
    print(S.score_dict)
    
if __name__ == "__main__":
    main()
