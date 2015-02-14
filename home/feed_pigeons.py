#coding=utf8
__author__ = '璐'

def feed(t):
    return t*(t+1)/2
def checkio(number):
    t = 0
    while(number>0):
        t+=1
        number -= feed(t)
    number += feed(t)
    return number if number >= feed(t-1) else feed(t-1)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"





