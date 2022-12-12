import copy
from os.path import join, dirname
import math, string
import pandas as pd
input="""
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

def solve(part=1, use_sample_data=True):
    allines=input.split('\n') if use_sample_data else open(join(dirname(__file__),"./input.txt")).readlines()
    charlines=[[*l] for l in allines[1:-1]] if use_sample_data else [[*l[:-1]] for l in allines]
    all_characters = list(string.ascii_letters)
    df = pd.DataFrame(data=charlines)
    print(df)
    found_solutions=[]
    rows = df.shape[0]
    cols = df.shape[1]
    def calc_diff_ok(curr, target):
        if curr=="S":
            return 1
        if target=="E" and curr=="z":
            return 1
        return (all_characters.index(target)-all_characters.index(curr))<=1

    def move(i,j, steps,visited={}):
        if len(found_solutions)>0 and steps>min(found_solutions):
            return
        visited[(i,j)]=(i,j)
        current_cell = df.iloc[i, j]
        #prevchar=path[-1:]
        #path=path+"." + current_cell
        if current_cell=="E" :
            print("Found E", steps)
            print(path)
            found_solutions.append(steps)
            return

        if (i+1)<rows and not (i+1,j) in visited:
            next_cell = df.iloc[i + 1, j]
            # Check if next_cell is close to letter in alphabet of current_cell so we can more there....
            # if so...
            if calc_diff_ok(current_cell, next_cell):
                move(i + 1, j, (steps+1),  copy.deepcopy(visited))

        #print("Checking upwards from ", (j, i))
        # Check one step to left (if not already been to (i-1,j) and inside df: i-1>=0
        if (i - 1) >=0 and not (i-1,j) in visited:
            next_cell = df.iloc[i - 1, j]
            # Check if next_cell is close to letter in alphabet of current_cell so we can more there....
            # if so...
            if calc_diff_ok(current_cell, next_cell):
                move(i - 1, j, (steps+1),copy.deepcopy(visited))

        #print("Checking right from ", (j, i))
        # Check one step tup (if not already been to (i,j-1) and inside df: j-1>=0
        if (j + 1) < cols and not (i,j+1) in visited:
            next_cell = df.iloc[i, j + 1]
            # Check if next_cell is close to letter in alphabet of current_cell so we can more there....
            # if so...
            if calc_diff_ok(current_cell, next_cell) :
                move(i, j + 1, (steps+1), copy.deepcopy(visited))

        #print("Checking left from ", (j, i))
        # Check one step tup (if not already been to (i,j+1) and inside df: j+1<=maxrows
        if (j-1)>=0 and not (i,j-1) in visited:
            next_cell = df.iloc[i, j - 1]
            # Check if next_cell is close to letter in alphabet of current_cell so we can more there....
            # if so...
            if calc_diff_ok(current_cell, next_cell) :
                move(i, j - 1,(steps+1),copy.deepcopy(visited))


    path=""
    move(0,0,1, {})
    print(found_solutions)

    print(min(found_solutions))