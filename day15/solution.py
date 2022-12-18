import copy
from os.path import join, dirname
import math, string
import pandas as pd
import json
from itertools import zip_longest
input="""
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""


def calc_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def solve(part=1, use_sample_data=True):
    pd.set_option('display.max_columns', None)
    #pd.set_option('display.max_rows', None)
    #pd.set_option('display.max_cols', None)
    allines=input.split('\n') if use_sample_data else open(join(dirname(__file__),"./input.txt")).readlines()
    sensor_objs={}
    sensors = []
    beacons = []
    beaconmap={}
    xvals=[]
    calculations=[]
    if use_sample_data:
        allines=allines[1:-1]
    for line in allines:
        text=line.split(": closest beacon is at ")
        sensorobj=None
        beaconobj=None
        for i in range(2):
            idxx=text[i].index("x=")
            idxx2 = text[i].index(",", idxx)
            idxy = text[i].index("y=")
            x = text[i][idxx + 2:idxx2]
            y=text[i][idxy+2:]
            if i==0:
                sensors.append((int(x), int(y)))
                sensorobj=(int(x), int(y))
            else:
                beacons.append((int(x), int(y)))
                beaconmap[(int(x), int(y))]=(int(x), int(y))
                beaconobj = (int(x), int(y))
            xvals.append(int(x))
        x=calc_distance(sensorobj[0],sensorobj[1], beaconobj[0], beaconobj[1])
        calculations.append((sensorobj[0],sensorobj[1],beaconobj[0],beaconobj[1], x))

        sensor_objs[sensorobj]=beaconobj
    target_row=10 if use_sample_data else 2000000

    map={}
    for sx, sy, bx, by, dist in calculations:
        d2=calc_distance(sx, sy, sx, target_row)
        if d2<=dist:
            diff=dist-d2
            for i in range(sx-diff, sx+diff+1):
                if (i, target_row) != (bx, by):  #Take awau Beacon
                    if i not in map:
                        map[i]=i
    print(len(map.keys()))
    map={}
    for sx, sy, bx, by, dist in calculations:
        for i in range(min(xvals), max(xvals)):
            d2=calc_distance(sx, sy, i, target_row)
            if d2<dist:
                #if (i, target_row) not in beaconmap:
                if i not in map:
                    map[i]=i
    print(len(map.keys()))

