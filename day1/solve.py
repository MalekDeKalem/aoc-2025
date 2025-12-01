import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--part", type=int, default=1, help="Select the part of the solution")
args = parser.parse_args()


with open("../input/input_1") as f:
    data = f.read().strip().split("\n") 

dial = 50
cnt = 0
if (args.part == 1):
    for d in data:
        if (d[0] == 'R'):
            dial = (dial + int(d[1:])) % 100
        else:
            dial = (dial - int(d[1:])) % 100

        if (dial == 0): cnt += 1

    print(cnt)
elif (args.part == 2):
    for d in data:
        num = int(d[1:])
        for _ in range(num):

            if (d[0] == 'R'):
                dial += 1
            else: 
                dial -= 1

            dial %= 100
            cnt += 1 if dial == 0 else 0
    print(cnt)

