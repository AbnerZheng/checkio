__author__ = '璐'
# get from MaxGraey, using the technic to identify whether a number is a fibonacci number:
#                       This is true if and only if one or both of 5x^2+4 or 5x^2-4 is a perfect square.
# wikipedia: http://en.wikipedia.org/wiki/Fibonacci_number#Recognizing_Fibonacci_numbers
from math import sqrt
def isSqr(x):
    return x == int(sqrt(x)) ** 2

def isFib(x):
    return isSqr(5 * x*x + 4) or isSqr(5 * x*x - 4)

def checkio(opacity):
    c = 10000
    x = 0
    while(1):
        c -= x if isFib(x) else -1
        if c == opacity:
            return x
        x += 1
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"


