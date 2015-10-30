__author__ = 'abnerzheng'

def r(xs,d):
    if isinstance(xs, list):
        for e in xs:r(e, d)
    else: d.append(xs)
def flat_list(xs):
    d=[];

    r(xs, d);return d


if __name__ == "__main__":
    print flat_list([1,2,3])
    assert flat_list([1, 2, 3]) == [1, 2, 3]
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]
