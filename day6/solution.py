import string
from os.path import join, dirname
input="zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"


def duplicates(word):
    for char in word:
        if word.count(char)>1:
            return True
    return False
def solve(part=1, use_sample_data=True):
    f=input if use_sample_data else open(join(dirname(__file__),"./input.txt")).read()
    for i in range(0,len(f)-4):
        if duplicates(f[i:i+4])==False:   #Loop until no duplicates found in substring
            print("Answer", i+4)
            break
