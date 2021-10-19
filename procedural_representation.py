from numpy import rot90
from puzzle import generate_puzzle, display_puzzle


PATH_BEGIN = [1, 4, 3, 6, 7, 8, 5, 2]
PATH_1 = [3, 6, 7, 8, 5, 4, 1, 0]
PATH_2 = [1, 4, 3, 6, 7, 8, 5, 2]
PATH_3 = [3, 6, 7, 8, 5, 4]


def move_one_step(puzzle, path):
    route = []
    for position in path:
        route.append(puzzle[position])
    tmp = route.pop(0)
    route.append(tmp)

    index = 0
    for position in path:
        puzzle[position] = route[index]
        index += 1
    display_puzzle(puzzle)
    return puzzle


def step_0(puzzle, path_begin):
    if puzzle[0] == 0:
        tmp = puzzle[1]
        puzzle[1] = 0
        puzzle[0] = tmp
    if puzzle[2] == 1 or puzzle[2] == 0:
        move_one_step(puzzle, path_begin)
        if puzzle[2] == 1 or puzzle[2] == 0:
            move_one_step(puzzle, path_begin)
    return puzzle


def step_1(puzzle, path_1):
    while puzzle[0] != 1:
        puzzle = move_one_step(puzzle, path_1)
    return puzzle


def step_2(puzzle, path_2):
    while puzzle[1] != 2:
        puzzle = move_one_step(puzzle, path_2)
    return puzzle


def step_3(puzzle, path_3):
    while puzzle[4] != 3:
        puzzle = move_one_step(puzzle, path_3)
    return puzzle


puzzle = generate_puzzle()
puzzle = step_0(puzzle, PATH_BEGIN)
puzzle = step_1(puzzle, PATH_1)
puzzle = step_2(puzzle, PATH_2)
puzzle = step_3(puzzle, PATH_3)
