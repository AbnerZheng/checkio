# coding=utf8
__author__ = '璐'


def count_neighbours(grid, row, col):
    NEIGHBORS = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
    cnt = 0
    for neighbor in NEIGHBORS:
        i, j = neighbor
        if 0 <= row + i < len(grid) and 0 <= col + j < len(grid[0]) and grid[row + i][col + j] == 1:
            cnt += 1
    return cnt


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(
        ((1, 0, 0, 1, 0),
         (0, 1, 0, 0, 0),
         (0, 0, 1, 0, 1),
         (1, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"

count_neighbours(((1, 0, 1, 0, 1),
                  (0, 1, 0, 1, 0),
                  (1, 0, 1, 0, 1),
                  (0, 1, 0, 1, 0),
                  (1, 0, 1, 0, 1),
                  (0, 1, 0, 1, 0),), 5, 4)