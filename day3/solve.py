import argparse
from collections import deque, Counter

parser = argparse.ArgumentParser()
parser.add_argument("--part", type=int, default=1, help="Select the part of the solution")
args = parser.parse_args()


with open("../input/input_3") as f:
    data = f.read().strip().split("\n") 

sum = 0
if (args.part == 1):
    for batteries in data:
        max_elem = max(batteries)
        max_index = batteries.index(max_elem)
        if (max_index < len(batteries)-1):
            second_elem = max(batteries[max_index+1:])
            sum += int(f"{max_elem}{second_elem}")
        else:
            second_elem = max(batteries[:max_index])
            sum += int(f"{second_elem}{max_elem}")

    print(sum)

elif (args.part == 2):
    k = 12
    for batteries in data:
        battery_list = list(batteries)
        battery_list.sort(reverse=True)
        k_list = []
        for i in range(k):
            k_list.append(battery_list[i])

        frequency_map = Counter(k_list)
        for battery in batteries:
            pass
            

        print(k_list)        

    print(sum)
