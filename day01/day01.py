from pathlib import Path
import numpy as np

input_path = Path(__file__).parent.joinpath("input.txt")

with open(input_path, "r") as f:
    raw_input = f.read().splitlines()

# print(raw_input)
count_gaps = sum(np.array(raw_input) == "")  # you can create the matrix from here

mat = np.zeros((count_gaps + 1, len(raw_input) - count_gaps), dtype=int)
vec = []
row_i = 0
for i, cal in enumerate(raw_input):
    if cal == "":
        row_i += 1
    else:
        mat[row_i, i - row_i] += 1
        vec += [cal]
# print(f"{mat=}")
# print(f"{vec=}")

elfs = mat @ np.array(vec, dtype=int).T
#  part 2
n = 3
vals = []
for _ in range(n):
    vals.append(max(elfs))
    elfs = elfs[elfs != vals[-1]]

print(sum(vals))

# if __name__ == "__main__"k:
