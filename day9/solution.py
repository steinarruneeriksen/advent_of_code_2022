from os.path import join, dirname
input="""
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

def move_knot(t1,t2):
    sum=(t1[0]+t2[0],t1[1]+t2[1])
    return sum

def distance(h,t):
    diff_x = abs(h[0] - t[0])
    diff_y = abs(h[1] - t[1])
    return max(diff_x, diff_y)


def adjust_tail(h, t):
    if distance(h,t)<2:
        return t  #No need to move

    if h[0] == t[0]:
        if h[1] - t[1] > 1:
            move = (0, 1)
        else:
            move = (0, -1)
    elif h[1] == t[1]:
        if h[0] - t[0] > 1:
            move = (1, 0)
        else:
            move = (-1, 0)
    else:
        if h[0] - t[0] > 1:
            move = (1,1) if t[1] < h[1] else (1,-1)
        elif h[0] - t[0] < - 1:
            move = (-1, 1) if t[1] < h[1] else (-1, -1)
        elif h[1] - t[1] >  1:
            move = (1, 1) if t[0] < h[0] else (-1, 1)
        elif h[1] - t[1] <  -1:
            move = (1, -1) if t[0] < h[0] else (-1, -1)
    return move_knot(t, move)

def solve(part=1, use_sample_data=True):

    allines=input.split('\n') if use_sample_data else open(join(dirname(__file__),"./input.txt")).readlines()
    if use_sample_data:
        allines=allines[1:-1]

    count=2 if part==1 else 10  # Only head + tail in part 1 so [(0,0),(0,0)] as starting list
    knots=count*[(0,0)]
    unique_positions={}
    for line in allines:
        if not use_sample_data:
            line=line[:-1]
        move_dir=line.split(" ")[0]
        move_len = int(line.split(" ")[1])
        for r in range(move_len):
            if move_dir=="R":
                update=(1,0)
            elif move_dir=="U":
                update=(0,1)
            elif move_dir=="D":
                update = (0, -1)
            elif move_dir=="L":
                update = (-1, 0)

            knots[0] = move_knot(knots[0], update)  # Move head
            # GO THOUGH OTHE KNOWS. IN PART 1 ONLY 1 EXTRA
            for knotidx in range(1,count):
                # Move each knot after the previous.
                # In part 1 there are only 2 so it is tail after head always
                knots[knotidx] = adjust_tail(knots[knotidx-1], knots[knotidx])

            # Check final tail
            if knots[count-1] not in unique_positions:
                unique_positions[knots[count-1]]=knots[count-1]

    print("Answer:",len(unique_positions.values()))
    print(unique_positions.values())