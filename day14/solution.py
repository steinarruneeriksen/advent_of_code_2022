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
    allines=input.split('\n') if use_sample_data else open(join(dirname(__file__),"./input.txt")).readlines()
