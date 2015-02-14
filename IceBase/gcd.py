__author__ = '璐'
gcd = lambda x,y: x if y==0 else gcd(y,x%y)
def greatest_common_divisor(*args):
    """
        Find the greatest common divisor
    """
    args = list(args)
    if len(args) == 1:
        return args[0]
    else:
        temp = gcd(args.pop(), args.pop())
        args.append(temp)
        return greatest_common_divisor(*args)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"

