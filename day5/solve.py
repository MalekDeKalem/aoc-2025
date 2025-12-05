import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--part", type=int, default=1, help="Select the part of the solution")
args = parser.parse_args()


with open("../input/input_5.txt") as f:
    data = f.read().strip().split("\n") 

cnt = 0


l = list()
is_over = False
i = 0
if (args.part == 1):
    for r in data:

        if r == '':
            is_over = True
            continue

        if not is_over:
            start, end = r.split("-")
            l.append((int(start), int(end)))
        else:
            for start, end in l:
                if int(r) >= start and int(r) <= end:
                    print(r)
                    cnt += 1
                    break


    print(cnt)
elif (args.part == 2):
    l = list()
    for r in data:
        start, end = r.split('-')
        l.append((int(start), int(end)))
    l.sort(key=lambda x: x[0])
    print(l)
    merged_ranges = []
    for k in range(len(l)-1):
        curr_start = l[k][0]
        curr_end = l[k][1]
        next_start = l[k+1][0]
        next_end = l[k+1][1]
        j = k+1
        while curr_end > next_start and j < len(l):
            curr_end = next_end
            next_end = l[j][1]
            next_start = l[j][0]
            j += 1
        k = j
        merged_ranges.append((curr_start, curr_end))
    print(merged_ranges) 


