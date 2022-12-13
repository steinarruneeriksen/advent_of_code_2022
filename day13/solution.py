import copy
from os.path import join, dirname
import math, string
import pandas as pd
import json
from itertools import zip_longest
input="""
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""


positive={}
def add_positive_pair(p):
    if p not in positive:
        positive[p]=p

negative={}
def add_negative_pair(p):
    if p not in negative:
        negative[p]=p

def solve(part=1, use_sample_data=True):
    allines=input.split('\n') if use_sample_data else open(join(dirname(__file__),"./input.txt")).readlines()

    def compare(d1,d2, pair):
        #print("Func", pair, d1,d2)
        for el in list(zip_longest(d1,d2)):
            if pair in negative:   #We have alrready detected a negative comparison
                return -1
            elif pair in positive:   #We have alrready detected a negative comparison
                return 1
            x, y = el[0], el[1]
            if x is None:
                add_positive_pair(pair)
                return 1
            if y is None:
                add_negative_pair(pair)
                return -1
            if isinstance(x, int) and isinstance(y, list):
                compare([x],y, pair)
            elif isinstance(x, list) and isinstance(y, int):
                compare(x,[y], pair)
            elif isinstance(x, list) and isinstance(y, list):
                compare(x,y, pair)
            else:
                if x<y:
                    add_positive_pair(pair)
                    return 1
                elif x > y:  #
                    add_negative_pair(pair)
                    return -1
            if pair in negative:   #We have alrready detected a negative comparison
                return -1
            elif pair in positive:   #We have alrready detected a negative comparison
                return 1
    pair=1
    if part==1:
        start_idx=1 if use_sample_data else 0
        for i in range(start_idx,len(allines), 3):
            dict1 = json.loads(allines[i])
            dict2 = json.loads(allines[i+1])
            v=compare(dict1,dict2, pair)
            pair=pair+1
        product=0
        for el in positive.values():
            product=product+el
        print(positive)
        print(product)
    else:
        initial_list = [[[2]],[[6]]]
        final_list = []
        start_idx = 1 if use_sample_data else 0
        for i in range(start_idx,len(allines), 3):
            initial_list.append(json.loads(allines[i]))
            initial_list.append(json.loads(allines[i+1]))
        n=0
        for i in range(len(initial_list)):
            put=False
            for j in range(len(final_list)):
                n=n+1
                v=compare(initial_list[i],final_list[j],n)
                if v<0:
                    put=True
                    final_list.insert(j,initial_list[i])
                    break
            if not put:
                final_list.append(initial_list[i])

        final_list.reverse()
        for f in final_list:
            print(f)
        id1 =final_list.index([[2]]) + 1
        id2 = final_list.index([[6]]) + 1  #+1 since it is zero indexed
        print(id1,id2)
        print("Final es is ", id1*id2)
