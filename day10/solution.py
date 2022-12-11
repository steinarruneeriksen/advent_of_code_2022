from os.path import join, dirname
input="""
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""
#
def check_print(cycle, crt):
    cycles_of_interest = [40, 80, 120, 160, 200, 240]
    if cycle in cycles_of_interest:
        print(crt)

def check_cycle(cycle, X, sumvalue, crt):
    #cycles_of_interest=[20, 60, 100, 140, 180, 220]
    cycles_of_interest = [40, 80, 120, 160, 200, 240]
    if cycle in cycles_of_interest:
        sumvalue+=(cycle*X)
    return sumvalue

def update_sprite(x):
    prefix = x - 1
    postfix = 39-(x+1)
    sprite = str(prefix * ".") + \
             str( 3 * "#") + \
             str(postfix * ".")
    return sprite

def update_crt(idx, crt, sprite):
    crt=crt[:idx] + sprite[idx] + crt[idx:39]
    return crt

def reset_crt():
    crt = 40*"."
    return crt

def solve(part=1, use_sample_data=True):
    allines=input.split('\n') if use_sample_data else open(join(dirname(__file__),"./input.txt")).readlines()
    if use_sample_data:
        allines=allines[1:-1]
    sprite=update_sprite(1)
    crt=40*""
    X=1
    cycle=0

    sumvalue=0
    for line in allines:
        crt = update_crt(cycle % 40, crt, sprite)
        instructions=line.split(" ")
        if len(instructions)==1:
            cycle += 1
            #sumvalue=check_cycle(cycle, X, sumvalue, crt)
            check_print(cycle, crt)
            crt = update_crt(cycle % 40, crt, sprite)
        else:
            inst=instructions[0]
            value = int(instructions[1])
            cycle += 1
            check_print(cycle, crt)
            crt=update_crt(cycle % 40, crt, sprite)
            cycle += 1
            check_print(cycle, crt)
            crt=update_crt(cycle % 40, crt, sprite)
            X += value
            sprite = update_sprite(X)
    #check_print(240, crt)
    print(sumvalue)


