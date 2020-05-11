import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from CopyCheck import copy_checker_by_filename

def main():
    df_sim1 = copy_checker_by_filename("HarmonicMean",test=True)
    df_sim2 = copy_checker_by_filename("Triangle",test=True)
    df_sim3 = copy_checker_by_filename("QuadEquation",test=True)
    
    df_sim1.to_csv("copycehck_HarmonicMean.csv")
    df_sim2.to_csv("copycehck_Triangle.csv")
    df_sim3.to_csv("copycehck_QuadEquation.csv")
    
if __name__ == "__main__":
    main()
    