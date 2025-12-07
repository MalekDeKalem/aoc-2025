import argparse
import math
parser = argparse.ArgumentParser()
parser.add_argument("--part", type=int, default=1, help="Select the part of the solution")
args = parser.parse_args()


with open("../input/input_6.txt") as f:
    data = f.read().strip().split("\n") 

res = 0
if (args.part == 1):
    l = list()
    for d in data:
        l.append(d.split())
    
    rows = len(l)
    cols = len(l[0])
    for c in range(cols):
        op = l[rows-1][c]
        nums = [int(l[r][c]) for r in range(rows-1)]
        if op == '+':
            res += sum(nums)
        elif op == '*':
            res += math.prod(nums)
    print(res)
elif (args.part == 2):
    pass


