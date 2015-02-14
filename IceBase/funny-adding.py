__author__ = '璐'
def checkio(data):
    """The sum of two integer elements"""
    a, b = data
    return a+b

if __name__ == '__main__':
    assert checkio([5, 5]) == 10, 'First'
    assert checkio([7, 1]) == 8, 'Second'
    print('All ok')