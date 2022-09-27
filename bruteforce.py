import copy
import time

def is_solution(coordinates, dimensions):
    # check if multiple queens on same row
    for x in range(dimensions):
        pos = coordinates[x]
        for next_col in range(x + 1, dimensions):
            next_pos = coordinates[next_col]
            # check if multiple queens on same row
            if pos == next_pos:
                return None
            # check if multiple queens on same diagonal
            if (pos + next_col - x) == next_pos:
                return None
            if (pos - next_col + x) == next_pos:
                return None
    return coordinates


def solvebf():
    solutions = []
    dim = 8
    dim = int(dim)
    times = []
    t = time.time()
    # populate this_permutation
    this_permutation = []
    for n in range(dim):
        this_permutation.append(0)

    # calculate the number of permutations
    possible_permutations = dim
    for n in range(dim):
        possible_permutations *= dim

    # initialize the counter
    #placement_cnt = 0

    # go through the permutations searching for all possible solutions
    for n in range(possible_permutations):
        rem = n
        for m in range(dim):
            this_permutation[m] = rem % dim
            rem //= dim
        # is this_permutation a solution?
        result = is_solution(copy.copy(this_permutation), dim)
        if result:

            # was this solution encountered previously?
            if result not in solutions:
                times.append(time.time()-t)
                solutions.append(result)
    return times
