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
minutes=[]
valves_open={}
valves_calc_pressure=[]
valves_parsed={}

def clear_maps():
    minutes.clear()
    valves_parsed.clear()
    valves_calc_pressure.clear()
    valves_open.clear()
map={}
def print_status():
    if len(valves_open.values())==0:
        print("No valves are open")
    else:
        st="Valves "
        for e in valves_open.values():
            st+=str(e)+ " and "
        st+=" are open, relaesing pressure " + str(curr_pressure() )
        print(st)
def curr_pressure():
    p=0
    for e in valves_open.keys():
        eobj = map[e]
        p+=eobj.flow
    return p
def tot_pressure():
    p=0
    for e in valves_calc_pressure:
        p+=e
    return p

class valve:
    def __init__(self, name, flow):
        self.name=name
        self.flow=flow
        self.tunnels=[]
        self.flow_tunnels=[]
    def __str__(self):
        tuns=""
        for t in self.tunnels:
            if t in map:
                el=map[t]
                tuns +="/" + str(el.name) + "(" + str(el.flow) + ")"
        return str(self.name) + "=>" + str(self.flow) + " " + tuns
    def preprocess(self, level):
        sum_flow=0
        if self.name not in valves_parsed:
            sum_flow=self.flow*level
        else:
            return 0#self.flow*level
        for t in self.tunnels:
            sub=map[t]
            valves_parsed[self.name] = self.name
            loc_sum=sub.preprocess(level+1)
            self.flow_tunnels.append((t,loc_sum*level))
            sum_flow+=loc_sum
        return sum_flow
    def process(self):
        if self.name not in valves_parsed:
            if self.name not in valves_open :
                minutes.append(1)
                print("== Minute " + str(len(minutes)) + " ==")
                print_status()
                print("You open valve ", self.name,len(minutes), (30-len(minutes))*self.flow)
                valves_open[self.name]=self.name
                valves_calc_pressure.append((30-len(minutes))*self.flow)
        else:
            return

        #for t in self.tunnels:
        sorted_by_second = sorted(self.flow_tunnels, key=lambda tup: tup[1], reverse=True)
        for t in sorted_by_second:
            sub=map[t[0]]
            valves_parsed[self.name] = self.name
            minutes.append(1)
            print("== Minute " + str(len(minutes)) + " ==")
            print_status()
            print("You move to ", sub.name)
            sub.process()

def print_preprocessed_map():
    for m in map:
        sub = map[m]
        print(sub.name)
        s="Flow tunnels:"

        for t in sub.flow_tunnels:
            s+=str(t)
        print(s)
        s="Ordered Flow tunnels:"
        sorted_by_second = sorted(sub.flow_tunnels, key=lambda tup: tup[1],  reverse=True)
        for t in sorted_by_second:
            s+=str(t)
        print(s)
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
        v=valve(vn, float(rate))
        text3=line.split("to valve")[1]
        text3=text3 if text3[0]!="s" else text3[1:]
        cols=text3.split(",")
        for c in cols:
            v.tunnels.append(c.strip())
        valves.append(v)

    for v in valves:
        map[v.name]=v
        print(v)
    v=map['AA']

    clear_maps()
    v.preprocess(1)
    print_preprocessed_map()
    clear_maps()
    v.process()

    print("TOT PRESS",tot_pressure())