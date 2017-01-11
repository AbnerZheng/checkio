# coding=utf8
# 这题就是线代中的求X^T * A = B^T 的解
# 转置一下,得 A^T * X = B
# 利用:$$ A^T *X = B =>(A^T)^{-1} * A^T * X = (A^T)^{-1}*B $$
# 通过一些列变换,将A^T变成I,运用这些变换到B,所获得的向量就是X的解

import copy

def solve(matrix,B):
    # 先转置
    inner_matrix = copy.deepcopy(matrix)
    for i in range(0, len(inner_matrix)):
        for j in range(i+1, len(inner_matrix)):
            inner_matrix[i][j], inner_matrix[j][i] = inner_matrix[j][i], inner_matrix[i][j]
    for i in range(0, len(inner_matrix)):  # 3*3矩阵
        if (inner_matrix[i][i] == 0):  # 如果对角线上的为0, 则要调换
            j = i + 1  # 下一行
            while j < len(inner_matrix):
                if inner_matrix[j][i] != 0:  # 不为0, 则交换
                    temp = inner_matrix[j]
                    inner_matrix[j] = inner_matrix[i]
                    inner_matrix[i] = temp
                    temp = B[j]
                    B[j] = B[i]
                    B[i] = temp
                    break
            if (j == len(inner_matrix)):
                print("error")
                return -1
        elif (inner_matrix[i][i] != 1):
            temp = inner_matrix[i][i]
            B[i] /= temp
            for kk in range(i, len(inner_matrix)):
                inner_matrix[i][kk] /= temp
        for k in range(i + 1, len(inner_matrix)):
            factor = float(inner_matrix[k][i]) / inner_matrix[i][i]
            B[k] -= factor * B[i]
            for m in range(i, len(inner_matrix[k])):
                inner_matrix[k][m] -= factor * inner_matrix[i][m]

    # 此时已经得到上三角矩阵
    for i in range(len(inner_matrix)-1, -1, -1):
        for j in range(i-1, -1, -1):
            factor = inner_matrix[j][i] / inner_matrix[i][i]
            B[j] -= B[i] * factor
    return B

def checkio(matrix):
    a = solve(matrix, [360,360,360])
    b = solve(matrix, [0,225,315])
    c = [0,0,0]

    for i in range(-5,5):
        for j in range(0, len(b)):
            c[j] = a[j]*i + b[j]
        if all(int(e) == e for e in c):
            break

    c =  [e % 360 if e%360<=180 else (e%360 - 360) for e in c]
    return  map(int, c)



# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':

    def check_it(func, matrix):
        result = func(matrix)
        if not all(-180 <= el <= 180 for el in result):
            print("The angles must be in range from -180 to 180 inclusively.")
            return False
        f, s, t = result
        temp = [0, 0, 0]
        temp[0] += f
        temp[1] += matrix[0][1] * f
        temp[2] += matrix[0][2] * f

        temp[0] += matrix[1][0] * s
        temp[1] += s
        temp[2] += matrix[1][2] * s

        temp[0] += matrix[2][0] * t
        temp[1] += matrix[2][1] * t
        temp[2] += t
        temp = [n % 360 for n in temp]
        if temp == [0, 225, 315]:
            return True
        else:
            print("This is the wrong final position {0}.".format(temp))
            return False
    #
    assert check_it(checkio,
                    [[1, 2, 3],
                     [3, 1, 2],
                     [2, 3, 1]]), "1st example"
    assert check_it(checkio,
                    [[1, 4, 2],
                     [2, 1, 2],
                     [2, 2, 1]]), "2nd example"
    assert check_it(checkio,
                    [[1, 2, 5],
                     [2, 1, 1],
                     [2, 5, 1]]), "3rd example"
