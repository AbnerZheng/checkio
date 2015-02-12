#coding=utf8
__author__ = '璐'

def checkio(data):
    """
        思路是按行遍历之后按列遍历  有等式b[i][j] = a[i][j]
    """
    rows, cols = len(data),len(data[0])
    result = []
    for i in range(cols):
        result.append([])
    for i,r in enumerate(data):
        #行遍历
        for j,c in enumerate(r):
            #列遍历
            result[j].append(c)
    return result

#someone else
def checkio2(matr):
    return [list(i) for i in zip(*matr)]



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]) == [[1, 4, 7],
                                    [2, 5, 8],
                                    [3, 6, 9]], "Square matrix"
    assert checkio([[1, 4, 3],
                    [8, 2, 6],
                    [7, 8, 3],
                    [4, 9, 6],
                    [7, 8, 1]]) == [[1, 8, 7, 4, 7],
                                    [4, 2, 8, 9, 8],
                                    [3, 6, 3, 6, 1]], "Rectangle matrix"

