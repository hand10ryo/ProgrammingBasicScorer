import subprocess

subprocess.run(['jupyter', 'nbconvert', '--to', 'script', './submit/*.ipynb'])