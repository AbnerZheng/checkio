__author__ = '璐'

from functools import reduce
from itertools import combinations
def break_rings(rings):
    # number of rings
    n_rings = max(reduce(set.union, rings))
    def trial(n):
        # rings for remove
        combi = combinations(range(1,n_rings+1), n)
        for c in combi:
            # count saved rings after removing rings
            rings_ = map(lambda x: len(x - set(c)), rings)
            if max(rings_) == 1:
                return True
        return False

    # brute force search
    for n in range(1, n_rings+1):
        if trial(n):
            return n
    return 0


# 递归
def break_rings_recurse(connections):
    if len(connections) == 0:
        return 0
    r1, r2 = connections[0]
    return min(
            break_rings_recurse([c for c in connections if r1 not in c]) + 1,
            break_rings_recurse([c for c in connections if r2 not in c]) + 1)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert break_rings(
        ({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(
        ({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 5}, {3, 6})) == 2, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {
        4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"





if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
    assert break_rings(({3,4},{5,6},{2,7},{1,5},{2,6},{8,4},{1,7},{4,5},{9,5},{2,3},{8,2},{2,4},{9,6},{5,7},{3,6},{1,3},)) == 5,"long chain2"
    assert break_rings(({1,2},{2,3},{3,4},{4,5},{5,2},{1,6},{6,7},{7,8},{8,9},{9,6},{1,10},{10,11},{11,12},{12,13},{13,10},{1,14},{14,15},{15,16},{16,17},{17,14},)) == 8,"13rd"

