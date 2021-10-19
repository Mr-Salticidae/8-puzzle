import random
import numpy as np


def generate_puzzle(dimension_size=3):
    puzzle = [i for i in range(dimension_size ** 2)]
    random.shuffle(puzzle)
    return puzzle


def display_puzzle(puzzle):
    print('-'*13)
    for i in range(len(puzzle)):
        if (i + 1) % np.sqrt(len(puzzle)) == 0:
            print(puzzle[i], end='|\n')
            print('-'*13)
        elif i % np.sqrt(len(puzzle)) == 0:
            print('|', puzzle[i], sep='', end=' '*4)
        else:
            print(puzzle[i], end=' '*4)
    print()
