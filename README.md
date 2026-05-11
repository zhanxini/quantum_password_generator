# quantum_password_generator
Two 10 word generators using: 
    1. EFF wordlist
    2. py diceware

INSTRUCTIONS: 

1. EFF wordlist
*this needs a little bit of work to get running*   

2. Python Diceware:
pip install dicewarepy before running python program

# wordlist source

1. eff internet wordlist source:
https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt

2. uses apparently multiple wordlists, needs a deep dive:
https://pypi.org/project/diceware/#is-it-secure

# randomness quality

Both methods have 10 randomly regenerated words which have **+128 bit of entropy**

for more reading: 
https://secure.research.vt.edu/diceware/#eff
