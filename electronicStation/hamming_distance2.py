#coding=utf8
__author__ = '璐'

def checkio_myself(n, m):
    return sum([int(e) for e in bin(n^m)[2:]])

checkio = lambda x,y:bin(x^y).count('1')
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
