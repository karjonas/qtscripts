import numpy as np
import quaternion
import itertools

def rotations():
    for x, y, z in itertools.permutations([0, 1, 2]):
        for sx, sy, sz in itertools.product([-1, 1], repeat=3):
            rotation_matrix = np.zeros((3, 3))
            rotation_matrix[0, x] = sx
            rotation_matrix[1, y] = sy
            rotation_matrix[2, z] = sz
            if np.linalg.det(rotation_matrix) == 1:
                yield quaternion.from_rotation_matrix(rotation_matrix)

all_rotations = list(rotations())
for rotation in all_rotations:
    print(rotation)