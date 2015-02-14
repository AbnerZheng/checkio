__author__ = '璐'

# veky has post a great solution for this:
# min, max = (lambda *args, key=None, r=r: sorted(args[0] if len(args) == 1
#     else args, key=key, reverse=r)[0] for r in range(2))


def min(*args, **kwargs):
    key = kwargs.get("key", lambda x:x)
    if len(args)==1:
       args = args[0]
    flag = False
    for e in args:
        if(not flag):
            result = e
            flag = True
        else:
            if key(e) < key(result):
                result = e
    return result




def max(*args, **kwargs):
    key = kwargs.get("key", lambda x:x)
    if len(args)==1:
       args = args[0]
    flag = False
    for e in args:
        if(not flag):
            result = e
            flag = True
        else:
            if key(e) > key(result):
                result = e
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"

