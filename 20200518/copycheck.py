import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from CopyChecker import copy_checker_by_filename

def main():
    df_sim1 = copy_checker_by_filename("Density")
    df_sim2 = copy_checker_by_filename("MonteCarlo")
    df_sim3 = copy_checker_by_filename("PrimeFactorization")
    
    df_sim1.to_csv("copycehck_Density.csv")
    df_sim2.to_csv("copycehck_MonteCarlo.csv")
    df_sim3.to_csv("copycehck_PrimeFactorization.csv")
    
if __name__ == "__main__":
    main()
    