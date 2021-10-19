from numpy import rot90
from puzzle import generate_puzzle, display_puzzle


PATH_BEGIN = [1, 4, 3, 6, 7, 8, 5, 2]
PATH_1 = [3, 6, 7, 8, 5, 4, 1, 0]
PATH_2 = [1, 4, 3, 6, 7, 8, 5, 2]
PATH_3 = [3, 6, 7, 8, 5, 4]
PATH_4 = [5, 8, 7, 6, 3]
PATH_5 = [3, 0, 1, 4, 5, 2, 1, 0, 3]


def rotate_one_step(puzzle, path):
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


def exchange(puzzle, target, path):
    for i in range(len(path) - 1):
        if puzzle[path[i]] == target and i < len(path) - 1:
            tmp = puzzle[path[i + 1]]
            puzzle[path[i + 1]] = target
            puzzle[path[i]] = tmp
        display_puzzle(puzzle)
    return puzzle


def step_0(puzzle, path_begin):
    print("Step 0")
    if puzzle[0] == 0:
        tmp = puzzle[1]
        puzzle[1] = 0
        puzzle[0] = tmp
    if puzzle[2] == 1 or puzzle[2] == 0:
        rotate_one_step(puzzle, path_begin)
        if puzzle[2] == 1 or puzzle[2] == 0:
            rotate_one_step(puzzle, path_begin)
    return puzzle


def step_1(puzzle, path_1):
    print("Step 1")
    while puzzle[0] != 1:
        puzzle = rotate_one_step(puzzle, path_1)
    return puzzle


def step_2(puzzle, path_2):
    print("Step 2")
    while puzzle[1] != 2:
        puzzle = rotate_one_step(puzzle, path_2)
    return puzzle


def step_3(puzzle, path_3):
    print("Step 3")
    if puzzle[2] == 0:
        tmp = puzzle[5]
        puzzle[5] = 0
        puzzle[2] = tmp
    while puzzle[4] != 3:
        puzzle = rotate_one_step(puzzle, path_3)
    return puzzle


def step_4(puzzle, path_4):
    print("Step 4")
    while puzzle[3] != 0:
        puzzle = rotate_one_step(puzzle, path_4)
    return puzzle


def step_5(puzzle, path_5):
    print("Step 5")
    puzzle = exchange(puzzle, 0, path_5)
    return puzzle


# def step_6(puzzle, path_6):
#     print("Step 6")
#     while puzzle[3] != 0:
#         puzzle = rotate_one_step(puzzle, path_6)
#     return puzzle


puzzle = generate_puzzle()
puzzle = step_0(puzzle, PATH_BEGIN)
puzzle = step_1(puzzle, PATH_1)
puzzle = step_2(puzzle, PATH_2)
puzzle = step_3(puzzle, PATH_3)
puzzle = step_4(puzzle, PATH_4)
puzzle = step_5(puzzle, PATH_5)
