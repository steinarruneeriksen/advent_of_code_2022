import copy
from os.path import join, dirname
import math, string
import pandas as pd
import json
from itertools import zip_longest
input="""
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

def solve(part=1, use_sample_data=True):
    #pd.set_option('display.max_rows', None)
    #pd.set_option('display.max_cols', None)
    allines=input.split('\n') if use_sample_data else open(join(dirname(__file__),"./input.txt")).readlines()
    paths=[]
    allcols=[]
    allrows=[]
    if use_sample_data:
        allines=allines[1:-1]
    for line in allines:
        cols=line.split(" -> ")
        path=[]
        for col in cols:
            x,y=col.split(",")
            allcols.append(int(x))
            allrows.append(int(y))
            path.append((int(x),int(y)))
        paths.append(path)

    print("Min,Max cols", min(allcols),  max(allcols))
    print("Min,Max rows", min(allrows), max(allrows))
    #df = pd.DataFrame(columns=list(range(min(allcols), max(allcols))))
    rows=[]
    if part==1:
        for i in range(max(allrows)+1):
            row={}
            for j in list(range(min(allcols), (max(allcols)+1))):
                row[j]="."
            rows.append(row)
    if part==2:
        for i in range(max(allrows) + 2):
            row = {}
            for j in list(range(0, 1000)):
                row[j] = "."
            rows.append(row)
        row = {}
        for j in list(range(0, 1000)):
            row[j] = "#"
        rows.append(row)
    #df.index=range(max(allrows))
    df = pd.DataFrame(data=rows)
    print(df[list(range(490,509))])

    #df.fillna(".")

    for path in paths:
        for i in range(0,len(path)-1):
            if path[i][0]==path[i+1][0]:
                if path[i][1]<path[i + 1][1]:
                    for x in range(path[i][1], path[i + 1][1]+1):
                        df.loc[x,path[i][0]]="#"
                else:
                    for x in range(path[i][1], path[i + 1][1]-1,-1):
                        df.loc[x,path[i][0]]="#"
            elif path[i][1]==path[i+1][1]:
                if path[i][0] < path[i + 1][0]:
                    for x in range(path[i][0], path[i+1][0]+1):
                        df.loc[path[i][1],x]="#"
                else:
                    for x in range(path[i][0], path[i+1][0]-1,-1):
                        df.loc[path[i][1],x]="#"

    print(df[list(range(490,509))])
    for i in range(100000):
        col=500
        n=0
        stable=False
        x=None
        y=None
        while not stable:
            if df.loc[0,500]=="o":
                print("We come to end.", i)
                print(df[list(range(490,509))])
                return
            if n == max(allrows)+2:
                print("Abyss.row..", i)
                print(df[list(range(490,509))])
                return
            while df.loc[n,col]==".":
                n=n+1
            n=n-1
            if col==0 or col==1000:
                print("Abyss...", i)
                print(df[list(range(490,509))])
                return
            if df.loc[n+1,col-1]==".":
                col=col-1
                n=n+1
            elif df.loc[n+1,col+1]==".":
                col = col + 1
                n=n+1
            else:
                stable=True
        df.loc[n, col] = "o"
    print(df[list(range(490,509))])
