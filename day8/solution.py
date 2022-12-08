import string
from os.path import join, dirname
import pandas as pd
import numpy as np
import sys
from scipy.signal import find_peaks
from scipy.signal import argrelextrema
from scipy.ndimage import maximum_filter
input="""
30373
25512
65332
33549
35390
"""


def solve(part=1, use_sample_data=True):

    allines=input.split('\n') if use_sample_data else open(join(dirname(__file__),"./input.txt")).readlines()
    charlines=[[*l] for l in allines[1:-1]] if use_sample_data else [[*l[:-1]] for l in allines]
    df = pd.DataFrame(data=charlines)
    print(df)
    df = df.astype(int)
    if part==1:
        count=0
        for i in range(df.shape[0]):  # iterate over rows
            for j in range(df.shape[1]):  # iterate over columns
                value = df.at[i, j]  # get cell value
                if i in [0,df.shape[0]-1] or j in [0,df.shape[1]-1]:
                    count+=1 #The edges
                else:
                    if value>df.iloc[0:i,j].max() or \
                        value>df.iloc[i+1:df.shape[0],j].max() or \
                        value>df.iloc[i,0:j].max() or \
                        value>df.iloc[i,j+1:df.shape[1]].max():
                        count+=1
        print("Part1 value", count)

    elif part==2:
        maxval=0
        def compare(v, lst, reverse=False):
            if len(lst)==0:
                return 0
            c=0
            if reverse:
                lst.reverse()
            for el in lst:
                if v>el:
                    c+=1
                else:
                    c+=1
                    break
            return c
        for i in range(df.shape[0]):  # iterate over rows
            for j in range(df.shape[1]):  # iterate over columns
                value = df.at[i, j]  # get cell value
                a=compare(value, df.iloc[0:i,j].tolist(), True)
                b=compare(value, df.iloc[i+1:df.shape[0],j].tolist())
                c=compare(value, df.iloc[i,0:j].tolist(), True)
                d=compare(value, df.iloc[i,j+1:df.shape[1]].tolist())
                prod=a*b*c*d
                print(prod, a,b,c,d)
                maxval=prod if prod>maxval else maxval
        print("Part2 max", maxval)



