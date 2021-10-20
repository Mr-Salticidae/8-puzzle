from time import time
from puzzle import Puzzle, generate_initial_state
from BFS import breadth_first_search
from procedural_representation import procedual_representation
from Astar_search import Astar_search

initial_state = generate_initial_state()
t0 = time()
procedual_representation(initial_state)
t1 = time()-t0
print('Procedual Representation')
print('Time:', t1)
print()

Puzzle.num_of_instances = 0
begin_time = time()
bfs = breadth_first_search(initial_state)
end_time = time()
print('BFS:', bfs)
print('Space:', Puzzle.num_of_instances)
print('Time:', end_time - begin_time)
print()

Puzzle.num_of_instances = 0
t0 = time()
astar = Astar_search(initial_state)
t1 = time() - t0
print('A*:', astar)
print('space:', Puzzle.num_of_instances)
print('time:', t1)
print()
