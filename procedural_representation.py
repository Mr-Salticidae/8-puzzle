from numpy import rot90
from puzzle import generate_puzzle, display_puzzle


PATH_BEGIN = [1, 4, 3, 6, 7, 8, 5, 2]
PATH_1 = [3, 6, 7, 8, 5, 4, 1, 0]
PATH_2 = [1, 4, 3, 6, 7, 8, 5, 2]
PATH_3 = [3, 6, 7, 8, 5, 4]
PATH_4 = [5, 8, 7, 6, 3]
PATH_5 = [3, 0, 1, 4, 5, 2, 1, 0, 3]
PATH_6 = [5, 8, 7, 6, 3, 4]
PATH_7 = [3, 4, 7, 6]
PATH_8 = [8, 7, 6, 3]
PATH_9 = [3, 0, 1, 2, 5, 4, 7, 8, 5, 2, 1, 0, 3]
PATH_10 = [3, 4, 7, 6]


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
    puzzle = exchange(puzzle, 0, path_4)
    return puzzle


def step_5(puzzle, path_5):
    print("Step 5")
    puzzle = exchange(puzzle, 0, path_5)
    return puzzle


# There are some bugs here. I got confused. Why can't it stop sometimes?
def step_6(puzzle, path_6):
    print("Step 6")
    while puzzle[5] != 4:
        puzzle = rotate_one_step(puzzle, path_6)
    return puzzle


def step_7(puzzle, path_7):
    print("Step 7")
    while puzzle[4] != 5:
        puzzle = rotate_one_step(puzzle, path_7)
    return puzzle


def step_8(puzzle, path_8):
    print("Step 8")
    puzzle = exchange(puzzle, 0, path_8)
    return puzzle


def step_9(puzzle, path_9):
    print("Step 9")
    puzzle = exchange(puzzle, 0, path_9)
    return puzzle


def step_10(puzzle, path_10):
    print("Step 10")
    while puzzle[4] != 0:
        puzzle = rotate_one_step(puzzle, path_10)
    return puzzle


puzzle = generate_puzzle()
puzzle = step_0(puzzle, PATH_BEGIN)
puzzle = step_1(puzzle, PATH_1)
puzzle = step_2(puzzle, PATH_2)
puzzle = step_3(puzzle, PATH_3)
if puzzle[2] != 2:
    puzzle = step_4(puzzle, PATH_4)
    puzzle = step_5(puzzle, PATH_5)
puzzle = step_6(puzzle, PATH_6)
if puzzle[8] != 5:
    puzzle = step_7(puzzle, PATH_7)
    puzzle = step_8(puzzle, PATH_8)
    puzzle = step_9(puzzle, PATH_9)
puzzle = step_10(puzzle, PATH_10)

if puzzle[3] == 8:
    print("Victory!")
else:
    print("Defeat...")
