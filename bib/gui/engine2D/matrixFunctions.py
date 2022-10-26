import math
import numpy as np

def translate(pos):
    tx, ty = pos

    return np.array([
        [1, 0, 0],
        [0, 1, 0],
        [tx, ty, 1]
    ])
