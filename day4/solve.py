import argparse
from queue import Queue
parser = argparse.ArgumentParser()
parser.add_argument("--part", type=int, default=1, help="Select the part of the solution")
args = parser.parse_args()


with open("../input/input_4.txt") as f:
    data = f.read().strip().split("\n") 

cnt = 0

dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1), (1, 0),  (1, 1)
]

rows = len(data)
cols = len(data[0])

if (args.part == 1):
    for r in range(rows):
        for c in range(cols):
            if data[r][c] == '@':
                neighbor_cnt = 0
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        neighbor_cnt += 1 if data[nr][nc] == '@' else 0
                cnt += 1 if neighbor_cnt < 4 else 0
    print(cnt)
elif (args.part == 2):
    while True:
        qu = Queue()
        for r in range(rows):
            for c in range(cols):
                if data[r][c] == '@':
                    pass
