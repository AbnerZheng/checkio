__author__ = '璐'
def min(*args, **kwargs):
    key = kwargs.get("key", lambda x:x)
    if len(args)>1:
        return [key(e) for e in list(args)].sort()[0]
    else:
        return [key(e) for e in args[0]].sort()[0]




def max(*args, **kwargs):
    key = kwargs.get("key", None)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"

