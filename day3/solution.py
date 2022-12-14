import string
from os.path import join, dirname
input="""
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
def common_member(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return set1 & set2

def solve(use_sample_data=True):
    lst=input.split() if use_sample_data else open(join(dirname(__file__),"./input.txt")).readlines()
    all_characters = list(string.ascii_letters)
    print(all_characters)
    sum=0
    for elf in lst:
        items=[*elf] #Each character
        half = len(items) // 2
        first_half = items[:half]
        sec_half = items[half:]
        common_item=common_member(first_half, sec_half)
        it=list(common_item)[0] # Assuming one common item:-)
        val=all_characters.index(it) + 1 # Index in alphabet + 1
        print(it, val)
        sum=sum+val
    print("Total sum ", sum)


