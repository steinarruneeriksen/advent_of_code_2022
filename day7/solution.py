import string
from os.path import join, dirname
input="""
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

class dir:
    def __init__(self, dirname, parent=None):
        self.dirname=dirname
        self.subdirs = {}
        self.files=[]
        self.parent=parent

    def add_sub_dir(self, name):
        if name not in self.subdirs:
            newdir=dir(name, self)  #Set self as parent
            self.subdirs[name]=newdir

    def add_file(self, name, size):
        if name not in self.subdirs:
            self.files.append((name, size))

    def find_sub_dir(self,name):
        if name in self.subdirs:
            return self.subdirs[name]
        return None


    def file_size_locally(self):
        size=0
        for f in self.files:
            size=size+int(f[1])
        return size

    def subdir_filesize(self, show_if_below_limit=None):
        special_sum=0
        tot_size=self.file_size_locally()
        for l in self.subdirs.values():
            t, s=l.subdir_filesize(show_if_below_limit)
            special_sum+=s
            tot_size+=t
        if show_if_below_limit is not None and tot_size<show_if_below_limit:
            special_sum+=tot_size
        return tot_size, special_sum

    def dirs_matching_size(self, required_size=None):
        dirs_matching=[]
        tot_size=self.file_size_locally()
        for l in self.subdirs.values():
            t, lst=l.dirs_matching_size(required_size)
            dirs_matching.extend(lst)
            tot_size+=t
        self.my_totsize=tot_size
        if tot_size>required_size:  # This dir is above size lim
            dirs_matching.append(self)
        return tot_size, dirs_matching

def solve(part=1, use_sample_data=True):
    top=dir("/")
    allines=input.split('\n') if use_sample_data else open(join(dirname(__file__),"./input.txt")).readlines()
    currnode=top
    for line in allines:
        currline=line if use_sample_data else line[:-1]
        if currline[:1]=="$":
            currline=currline[2:]
            if currline[:2]=="cd":
                dname=currline.split(" ")[1] #SECOND FIELD
                if dname=="/":
                    #print("Move to top node")
                    currnode=top
                elif dname=="..":
                    #print("Move upwards from", currnode.dirname)
                    currnode=currnode.parent
                else:
                    #print("Move to subdir", dname)
                    currnode=currnode.find_sub_dir(dname)
        elif currline[:3]=="dir":
            dname=currline.split(" ")[1] #SECOND FIELD
            currnode.add_sub_dir(dname)
        elif len(currline)>1:
            content=currline.split(" ")
            currnode.add_file(name=content[1], size=int(content[0]))

    if part==1:
        tot_size, special_sum=top.subdir_filesize(100000)
        print("Sum of dirs below limit",special_sum)
    else:
        tot_space=70000000
        req_space=30000000
        tot_size, special_sum = top.subdir_filesize(0)
        rem_space=tot_space-tot_size
        req_deletion=req_space-rem_space
        print("Required deletion size", req_deletion)
        totsize, matchlist=top.dirs_matching_size(req_deletion)
        def size_prop(elem):
            return elem.my_totsize
        matchlist.sort(key=size_prop, reverse=False)
        print("Smallest dir large than limit", matchlist[0].dirname,matchlist[0].my_totsize)



