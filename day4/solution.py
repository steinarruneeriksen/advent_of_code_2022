import string
from os.path import join, dirname
input="""
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
def prettyprint(lst1, lst2, max_length=100):
    def print_elf(lst):
        string_val = "." * max_length
        new_substring = "".join(str(el) for el in lst)
        string_val=string_val[:lst[0]-1] + new_substring + string_val[lst[len(lst)-1]:]
        print(string_val)
    print_elf(lst1)
    print_elf(lst2)


def one_contains_the_other(set1, set2):
    if set1.issubset(set2) or set2.issubset(set1):
        return True
    return False

def create_list(elf_range):
    range_elem=elf_range.split("-")
    return list(range(int(range_elem[0]), int(range_elem[1])+1))

def solve(use_sample_data=True):
    lst=input.split() if use_sample_data else open(join(dirname(__file__),"./input.txt")).readlines()
    count=0
    for pair in lst:
        elves=pair.split(",")
        elf1 = create_list(elves[0])
        elf2 = create_list(elves[1])
        prettyprint(elf1, elf2, 10 if use_sample_data else 100)
        b=one_contains_the_other(set(elf1), set(elf2))
        if b:
            count += 1
            print("One contains the other")
        print("")
    print("Total number ", count)


