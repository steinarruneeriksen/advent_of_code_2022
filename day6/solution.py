import string
from os.path import join, dirname
input="mjqjpqmgbljsphdztnvjfqwrcgsmlb"


def duplicates(word):
    for char in word:
        if word.count(char)>1:
            return True
    return False
def solve(part=1, use_sample_data=True):
    seqsize=4 if part==1 else 14
    print("Searching fod sequences of size ", seqsize)
    f=input if use_sample_data else open(join(dirname(__file__),"./input.txt")).read()
    for i in range(0,len(f)-seqsize):
        if duplicates(f[i:i+seqsize])==False:   #Loop until no duplicates found in substring
            print("Answer", i+seqsize)
            break
