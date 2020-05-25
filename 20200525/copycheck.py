import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from CopyChecker import copy_checker_by_filename

def main():
    df_sim1 = copy_checker_by_filename("MatrixMatrix")
    df_sim2 = copy_checker_by_filename("Power20")
    
    df_sim1.to_csv("copycehck_Density.csv")
    df_sim2.to_csv("copycehck_MonteCarlo.csv")
    
if __name__ == "__main__":
    main()
    