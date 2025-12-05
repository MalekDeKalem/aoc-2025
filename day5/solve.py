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
    pass
