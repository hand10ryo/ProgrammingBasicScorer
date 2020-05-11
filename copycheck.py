import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Scorer import CopyCheck

def main():
    C = CopyCheck(os.getcwd())
    C.check("MatrixMatrix")
    
if __name__ == "__main__":
    main()
    