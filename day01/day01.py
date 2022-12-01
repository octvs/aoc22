from pathlib import Path
import numpy as np

input_path = Path(__file__).parent.joinpath("test-input.txt")

with open(input_path, "r") as f:
    raw_input = f.read().splitlines()

print(raw_input)

mat = np.array([], dtype=int)
vec = []
for i in raw_input:
    if i == "":
        new_row = np.hstack([np.zeros((1, mat.shape[1])), 1])
        mat = np.vstack([np.hstack([mat, 0]), new_row])
    else:
        mat = np.hstack([mat, 1])
        vec += [i]

    print(f"{mat=}")
    print(f"{vec=}")

# if __name__ == "__main__":
