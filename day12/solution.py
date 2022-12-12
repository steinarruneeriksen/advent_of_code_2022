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

    def breadth_first_search(starting):
        q=[]
        visited = {}
        levels = {}
        visited[starting]=starting
        levels[starting]=1
        q.append(starting)
        qmap={}
        qmap[starting]=starting
        while len(q)>0:
            node = q.pop(0)
            current_cell = df.iloc[node[0], node[1]]
            if current_cell == "z":
                print("Found E", levels[node])
                found_solutions.append(levels[node])
                qmap.pop(node)
                continue

            check1=(node[0] + 1, node[1])
            if (node[0] + 1) < rows and  not check1 in qmap:
                next_cell = df.iloc[node[0]+1, node[1]]
                if calc_diff_ok(current_cell, next_cell):
                    levels[check1] = levels[node] + 1
                    q.append(check1)
                    qmap[check1]=check1

            check2 = (node[0] - 1, node[1])
            if (node[0] - 1) >= 0 and not check2  in qmap:#in visited:
                next_cell = df.iloc[node[0]- 1, node[1]]
                if calc_diff_ok(current_cell, next_cell):
                    levels[check2] = levels[node] + 1
                    q.append(check2)
                    qmap[check2] = check2

            check3 = (node[0], node[1] + 1)
            if (node[1] + 1) < cols and not check3 in qmap:#visited:
                next_cell = df.iloc[node[0], node[1]+1]
                if calc_diff_ok(current_cell, next_cell):
                    levels[check3] = levels[node] + 1
                    q.append(check3)
                    qmap[check3] = check3

            check4 = (node[0], node[1] - 1)
            if (node[1] - 1) >= 0 and not check4 in qmap:#visited:
                next_cell = df.iloc[node[0], node[1]-1]
                if calc_diff_ok(current_cell, next_cell):
                    levels[check4] = levels[node] + 1
                    q.append(check4)
                    qmap[check4] = check4

            #qmap.pop(node)

    def move(i,j, steps,visited={}):
        if len(found_solutions)>0 and steps>min(found_solutions):
            return
        visited[(i,j)]=(i,j)
        current_cell = df.iloc[i, j]
        if current_cell=="z" :
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
    #move(0,0,1, {})
    if part==1:
        breadth_first_search((0,0))
    else:
        for i in range(df.shape[0]):  # iterate over rows
            for j in range(df.shape[1]):  # iterate over columns
                current_cell = df.iloc[i, j]
                if current_cell=="a":
                    print("Staing from ",(i, j))
                    breadth_first_search((i, j))

    print(found_solutions)
    print(min(found_solutions))