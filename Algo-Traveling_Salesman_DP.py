###############################################
# First solution
###############################################
'''
Salesman does not return to the starting point
Returns the short path

Blog post: https://towardsdatascience.com/solving-tsp-using-dynamic-programming-2c77da86610d

GitHub: https://github.com/DalyaG/CodeSnippetsForPosterity/tree/master/SolvingTSPUsingDynamicProgramming
'''

# %%
def DP_TSP(distances_array):
    n = len(distances_array) # number of cities to visit
    all_points_set = set(range(n))

    # memo keys: tuple(sorted_points_in_path, last_point_in_path)
    # memo values: tuple(cost_thus_far, next_to_last_point_in_path)
    memo = {(tuple([i]), i): tuple([0, None]) for i in range(n)}
    queue = [(tuple([i]), i) for i in range(n)]

    while queue:
        prev_visited, prev_last_point = queue.pop(0)
        prev_dist, _ = memo[(prev_visited, prev_last_point)]

        to_visit = all_points_set.difference(set(prev_visited))
        for new_last_point in to_visit:
            new_visited = tuple(sorted(list(prev_visited) + [new_last_point]))
            new_dist = prev_dist + distances_array[prev_last_point][new_last_point]

            if (new_visited, new_last_point) not in memo:
                memo[(new_visited, new_last_point)] = (new_dist, prev_last_point)
                queue += [(new_visited, new_last_point)]
            else:
                if new_dist < memo[(new_visited, new_last_point)][0]:
                    memo[(new_visited, new_last_point)] = (new_dist, prev_last_point)

    optimal_path, optimal_cost = retrace_optimal_path(memo, n)

    return optimal_path, optimal_cost

def retrace_optimal_path(memo, n):
    points_to_retrace = tuple(range(n))

    full_path_memo = dict((k, v) for k, v in memo.items() if k[0] == points_to_retrace)
    path_key = min(full_path_memo.keys(), key=lambda x: full_path_memo[x][0])

    last_point = path_key[1]
    optimal_cost, next_to_last_point = memo[path_key]

    optimal_path = [last_point]
    points_to_retrace = tuple(sorted(set(points_to_retrace).difference({last_point})))

    while next_to_last_point is not None:
        last_point = next_to_last_point
        path_key = (points_to_retrace, last_point)
        _, next_to_last_point = memo[path_key]

        optimal_path = [last_point] + optimal_path
        points_to_retrace = tuple(sorted(set(points_to_retrace).difference({last_point})))

    return optimal_path, optimal_cost

distances_array = [[0, 10, 15, 20], 
                   [10, 0, 35, 25], 
                   [15, 35, 0, 30], 
                   [20, 25, 30, 0]]
DP_TSP(distances_array)

# %%
###############################################
# Second solution
###############################################
'''
Salesman returns to the starting point

https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/
'''

import sys
from itertools import permutations

V = 4 # number of vertices
 
# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
 
    # store all vertex apart from source vertex
    # if s = 0, then vertex = range(1, V)
    vertex = [v for v in range(V) if v != s]
 
    # store minimum weight Hamiltonian Cycle
    min_path = sys.maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
 
        # store current Path weight(cost)
        current_pathweight = 0
 
        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
 
        # update minimum
        min_path = min(min_path, current_pathweight)
         
    return min_path
 
# matrix representation of graph
graph = [[0, 10, 15, 20], 
         [10, 0, 35, 25],
         [15, 35, 0, 30], 
         [20, 25, 30, 0]]
s = 0
print(travellingSalesmanProblem(graph, s))

# %%
###############################################
# Third solution
###############################################

from itertools import combinations

def solve_tsp_dynamic(distances_array, N):
    A = {(frozenset([0, idx + 1]), idx + 1): (dist, [0, idx + 1]) for idx, dist in enumerate(distances_array[0][1:])}
    for m in range(2, N):
        B = {}
        for S in [frozenset(C) | {0} for C in combinations(range(1, N), m)]:
            for j in S - {0}:
                B[(S, j)] = min([(A[(S - {j}, k)][0] + distances_array[k][j], A[(S - {j}, k)][1] + [j]) for k in S if k != 0 and k != j])
        A = B

    # res is a tuple (min_cost, min_path)
    res = min([(A[d][0] + distances_array[0][d[1]], A[d][1]) for d in iter(A)])
    return res[0]

distances_array = [[0, 10, 15, 20], 
                   [10, 0, 35, 25], 
                   [15, 35, 0, 30], 
                   [20, 25, 30, 0]]
solve_tsp_dynamic(distances_array, 4)
# %%
