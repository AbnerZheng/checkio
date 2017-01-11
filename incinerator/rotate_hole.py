class Circular(object):
    def __init__(self, data, pipe_numbers):
        self.start = 0
        self.state = data
        self.len = len(data)
        self.pipe_numbers = pipe_numbers

    def cround(self, i):
        self.start = self.len - i

    def satisfy(self):
        for e in self.pipe_numbers:
            i = (self.start + e) % self.len
            if self.state[i] == 0:
                return False
        return True


def rotate(state, pipe_numbers):
    c = Circular(state, pipe_numbers)
    result = []
    for i in range(len(state)):
        c.cround(i)
        if c.satisfy():
            result.append(i)
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"
