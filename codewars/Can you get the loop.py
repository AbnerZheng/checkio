def loop_size(node):
    first = node
    two = node

    def go_once(n, c):
        return (n.next, c + 1)

    def go_twice(n,c):
        return (n.next.next, c + 2)

    (first, c_first) = go_once(first, 0)
    (two, c_twice) = go_twice(two, 0)

    while first != two:
        (first, c_first) = go_once(first, c_first)
        (two, c_twice) = go_twice(two, c_twice)
    return c_twice - c_first
