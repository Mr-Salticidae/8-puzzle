import random
import numpy as np


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


def generate_puzzle(dimension_size=3):
    puzzle = [i for i in range(dimension_size ** 2)]
    random.shuffle(puzzle)
    display_puzzle(puzzle)
    return puzzle


class Puzzle:
    goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    heuristic = None
    evaluation_function = None
    needs_hueristic = False
    num_of_instances = 0

    def __init__(self, state, parent, action, path_cost, needs_heuristic=False):
        self.state = state
        self.parent = parent
        self.action = action

        if parent:
            self.path_cost = parent.path_cost + path_cost
        else:
            self.path_cost = path_cost

        if needs_heuristic:
            self.needs_hueristic = True
            self.generate_heuristic()
            self.evaluation_function = self.heuristic + self.path_cost

        Puzzle.num_of_instances += 1

    def __str__(self):
        return str(self.state[0:3]) + '\n' + str(self.state[3:6]) + '\n' + str(self.state[6:9])

    def generate_heuristic(self):
        self.heuristic = 0
        for num in range(1, 9):
            distance = abs(self.state.index(num) - self.goal_state.index(num))
            i = int(distance / 3)
            j = int(distance % 3)
            self.heuristic = self.heuristic + i + j

    def goal_test(self):
        if self.state == self.goal_state:
            return True
        return False

    @staticmethod
    def find_valid_actions(i, j):
        valid_actions = ['U', 'D', 'L', 'R']

        if i == 0:
            valid_actions.remove('U')
        elif i == 2:
            valid_actions.remove('D')

        if j == 0:
            valid_actions.remove('L')
        elif j == 2:
            valid_actions.remove('R')
        return valid_actions

    def generate_child(self):
        children = []
        x = self.state.index(0)
        i = int(x / 3)
        j = int(x % 3)
        valid_actions = self.find_valid_actions(i, j)

        for action in valid_actions:
            new_state = self.state.copy()
            if action is 'U':
                new_state[x], new_state[x - 3] = new_state[x - 3], new_state[x]
            elif action is 'D':
                new_state[x], new_state[x + 3] = new_state[x + 3], new_state[x]
            elif action is 'L':
                new_state[x], new_state[x - 1] = new_state[x - 1], new_state[x]
            elif action is 'D':
                new_state[x], new_state[x + 1] = new_state[x + 1], new_state[x]
            children.append(
                Puzzle(new_state, self, action, 1, self.needs_hueristic))
        return children

    def find_solution(self):
        solution = []
        solution.append(self.action)
        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.action)
        solution = solution[:-1]
        solution.reverse()
        return solution
