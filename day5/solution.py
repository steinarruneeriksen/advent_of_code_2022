import string
from os.path import join, dirname
input="""
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""



def solve(part=1, use_sample_data=True):
    lst=input.split('\n') if use_sample_data else open(join(dirname(__file__),"./input.txt")).readlines()
    if use_sample_data:
        lst=lst[1:-1]  #LINE BREAKS AT START AND END
    linelengths=[len(x.strip()) for x in lst]
    split_idx=linelengths.index(0)  #Line with space
    map={}
    for i in range(1,10):
        map[i]=[]   #Create map with 9 arrays for each stack

    for i in range(split_idx-2, -1, -1):  # Loop reverse order to push onto stack
        def parse_line(line):
            idx=1
            for i in range(0,len(line), 4): #step 4 forwardr (brackets, content + space)
                substr=line[i:i+3]
                if len(substr.strip())>0:  #Assign only non empty columns
                    map[idx].append(substr)
                idx=idx+1
        parse_line(lst[i])
    print(map)

    for line in lst[split_idx+1:] : #Remainser of rows
        line=line.replace('\n','') #Get rid of line break
        cols=line.split(' ')
        move_count=int(cols[1]) # second field is count
        from_col = int(cols[3])  # second field is count
        to_col = int(cols[5])  # second field is count
        if part==1:
            for c in range(move_count):
                elem=map[from_col].pop()
                map[to_col].append(elem)
        else: # Part 2
            complete_list=map[from_col]
            map[from_col]=complete_list[:-move_count] #Same as popping move_count times
            map[to_col].extend(complete_list[-move_count:])  #Extend this list
    print(map)
    solution_word=""
    for val in map.values():
        if len(val)>0:
            last=val.pop()
            solution_word +=str(last[1:-1]) # APPEND CONTENT - FRONT AND ENDING BRACKET
    print(solution_word)



