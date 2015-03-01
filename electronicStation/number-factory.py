__author__ = '璐'
import functools
def factorize(n):
    i,result = 2 , []
    while (n != 1):
        if n % i == 0:
            n//=i
            if i > 10:
                return False
            result.append(i)
        else:
            i+=1
    return result

def checkio(number):
    fact = factorize(number)
    if not fact:
        return 0
    num_2 , num_3= fact.count(2) , fact.count(3)
    a,b = num_2//3, num_2%3
    for e in range(a):
        fact.remove(2)
        fact.remove(2)
        fact.remove(2)
        fact.append(8)
    c,d = num_3//2, num_3%2
    for e in range(c):
        fact.remove(3)
        fact.remove(3)
        fact.append(9)
    for e in range(d):
        if b:
            fact.remove(3)
            fact.remove(2)
            fact.append(6)
            b-=1
        else:
            break
    b //= 2
    for e in range(b):
        fact.remove(2)
        fact.remove(2)
        fact.append(4)
    return int(functools.reduce(lambda x,y:str(x)+str(y),sorted(fact)))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
    assert checkio(10) == 25, "10"
    assert checkio(12) == 26, "12"

