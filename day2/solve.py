import argparse
import itertools

parser = argparse.ArgumentParser()
parser.add_argument("--part", type=int, default=1, help="Select the part of the solution")
args = parser.parse_args()


with open("../input/input_2") as f:
    data = f.read().strip().split(",") 

sum = 0
if (args.part == 1):
    for rang in data: 
        start, end = rang.split("-")
        for i in range(int(start), int(end) + 1):
            id = str(i)
            if (len(id) % 2 != 0):
                continue
            sum += i if id[:len(id)//2] == id[len(id)//2:] else 0
    print(sum)
elif (args.part == 2):
    pass
