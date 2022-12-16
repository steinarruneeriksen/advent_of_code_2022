import copy
from os.path import join, dirname
import math, string

input="""
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""

class valve:
    def __init__(self, name, flow):
        self.name=name
        self.flow=flow
        self.tunnels=[]
    def __str__(self):
        tuns=""
        for t in self.tunnels:
            tuns +="/" + t
        return self.name + "=>" + str(self.flow) + " " + tuns

def solve(part=1, use_sample_data=True):

    allines=input.split('\n') if use_sample_data else open(join(dirname(__file__),"./input.txt")).readlines()
    valves=[]
    if use_sample_data:
        allines=allines[1:-1]

    for line in allines:
        text=line.split(" ")
        vn=text[1]
        text2=line.split("has flow rate=")
        rate=text2[1][:text2[1].index(";")]
        print(valve, rate)
        v=valve(vn, float(rate))
        valves.append(v)
        text3=line.split("tunnels lead to valve")[1]
        print (text3)
        text3=text3 if text3[0]!="s" else text3[1:]
        cols=text3.split(",")
        for c in cols:
            v.tunnels.append(c.strip())
    for v in valves:
        print(v)

    