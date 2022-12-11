from os.path import join, dirname
import math
input="""
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

monkeymap={}
def find_common_divisor():
    p=1
    for v in monkeymap.values():
        p=p*v.test_arg
    return p

def cust_mod_isint(x,v):
    return (x % v)==0

def addition_operation(val, arg):
    #print("Operation : adding ", val, arg, (val+arg))
    return val + arg
def product_operation(val, arg):
    #print("Operation : multiplying ", val, arg, (val*arg))
    return val * arg
def expon_operation(val, arg):
    #print("Operation : exponential ", val, arg, (val*val))
    return val ** arg

class monkey():


    def __init__(self, idx, starting_items, operating_func, operation_arg, test_arg, pos_test_monkey, neg_test_monkey, part=1):
        self.idx=idx
        self.items=starting_items
        self.operating_func = operating_func
        self.operation_arg = operation_arg
        self.test_arg = test_arg
        self.pos_test_monkey=pos_test_monkey
        self.neg_test_monkey=neg_test_monkey
        self.inspected=0
        self.part=part


    def pass_item(self, item):
        self.items.append(item)


    def run_operations(self):
        self.inspected=self.inspected+len(self.items)
        for item in self.items:
            #print("Monkey", self.idx, "inspecting", item)
            v=self.operating_func(item, self.operation_arg)
            if self.part==1:
                v=math.floor(v/3)
            else:
                v = (v % find_common_divisor())
            passmonkey=self.test_which_monkey_to_pass(v)
            monkeymap[passmonkey].pass_item(v)
        self.items=[]

    def test_which_monkey_to_pass(self, worry_lev):
        if cust_mod_isint(worry_lev,self.test_arg):
            return self.pos_test_monkey
        else:
            return self.neg_test_monkey


    def __str__(self):
        s="Monkey " + str(self.idx) + " holds " + str(self.items) + " inspected " + str(self.inspected)
        return s


def solve(part=1, use_sample_data=True):
    #print(int(231871064940156750 // 5), 231871064940156750 / 5 % 100)
    #return
    allines=input.split('\n') if use_sample_data else open(join(dirname(__file__),"./input.txt")).readlines()
    prefix1 = "  Starting items:"
    prefix2 = "  Operation:"
    prefix3 = "  Test:"
    prefix4 = "    If true: throw to monkey"
    prefix5 = "    If false: throw to monkey"

    divide_res=True if part==1 else False
    currrent_monkey_idx=0
    divisible_by=0
    pos_pass_monkey=0
    neg_pass_monkey=0
    current_oper=None
    current_oper_arg = 0
    current_items=[]
    for line in allines:
        if use_sample_data==False:
            line = line[:-1]
        print(line)
        if line[0:6]=="Monkey":
            currrent_monkey_idx=int(line.split(" ")[1][:-1])  #Remove : befoe converting to int
        if line[0:len(prefix1)] == prefix1:
            items=line[len(prefix1):].split(",")
            current_items=[int(x) for x in items]
        if line[0:len(prefix2)] == prefix2:
            cols=line.split(" ")
            oper = cols[len(cols) - 2]
            num = cols[len(cols) - 1]
            if oper=="+":
                current_oper=addition_operation
                if num=="old":
                    current_oper = product_operation
                    current_oper_arg = 2   # Old * 2
                else:
                    current_oper_arg=int(num)
            elif oper=="*":
                current_oper=product_operation
                if num=="old":
                    current_oper = expon_operation
                    current_oper_arg = 2   # Old exponential with 2
                else:
                    current_oper_arg=int(num)
        if line[0:len(prefix3)] == prefix3:
            cols=line.split(" ")
            divisible_by=int(cols[len(cols)-1])
        if line[0:len(prefix4)] == prefix4:
            cols=line.split(" ")
            pos_pass_monkey=int(cols[len(cols)-1])
        if line[0:len(prefix5)] == prefix5:
            cols=line.split(" ")
            neg_pass_monkey=int(cols[len(cols)-1])
        if len(line.strip())==0:
            monkeymap[currrent_monkey_idx]=monkey(currrent_monkey_idx, current_items,
                                                  current_oper, current_oper_arg, divisible_by, pos_pass_monkey, neg_pass_monkey, part)

    monkeymap[currrent_monkey_idx] = monkey(currrent_monkey_idx, current_items,
                                            current_oper, current_oper_arg, divisible_by, pos_pass_monkey,neg_pass_monkey, part)
    for v in monkeymap.values():
        print(v)

    rounds=20 if part==1 else 10000
    for x in range(rounds):
        #print("Calculating round ", x)
        for v in monkeymap.values():
            v.run_operations()

    monkeylist=list(monkeymap.values())

    def list_sorter(elem):
        return elem.inspected
    # Sorting by monkeys on how many inspected items
    monkeylist.sort(key=list_sorter, reverse=True)
    for m in monkeylist:
        print(m)

    final_product=1
    for v in monkeylist[:2]:  #THE TOP 2 MONKEYS
        final_product=final_product*v.inspected
    print("FINAL", final_product)