from numpy import rot90
from puzzle import generate_puzzle, display_puzzle


PATH_BEGIN = [1, 4, 3, 6, 7, 8, 5, 2]
PATH_1 = [3, 6, 7, 8, 5, 4, 1, 0]


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
    return puzzle


def init(puzzle, path_begin):
    if puzzle[0] == 0:
        tmp = puzzle[1]
        puzzle[1] = 0
        puzzle[0] = tmp
    if puzzle[2] == 1 or puzzle[2] == 0:
        move_one_step(puzzle, path_begin)
        if puzzle[2] == 1 or puzzle[2] == 0:
            move_one_step(puzzle, path_begin)
    return puzzle


puzzle = generate_puzzle()
display_puzzle(puzzle)
puzzle = init(puzzle, PATH_BEGIN)
display_puzzle(puzzle)
