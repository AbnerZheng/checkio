__author__ = '璐'
def count_gold(pyramid):
    result = [0]*len(pyramid[-1])
    for e in pyramid:
        for dummy_i in range(len(e)-1,0-1,-1):
            result[dummy_i]=max(result[dummy_i]+e[dummy_i],result[dummy_i-1]+e[dummy_i]if dummy_i>0 else 0 )
    return max(result)


def count_gold2(pyramid):
    def count(pyramid, level, to, number):
        here = number + pyramid[level][to]
        if level == len(pyramid) - 1:
            return here
        else:
            return max(
              count(pyramid, level + 1, to, here) ,
              count(pyramid, level + 1, to + 1, here),
            )
    return count(pyramid, 0, 0, 0)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold2((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold2((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"

