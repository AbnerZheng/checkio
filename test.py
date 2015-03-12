def fibgolf(s, u):
    if s == 'perrin' or s == 'tribonacci' or s == 'padovan':
        if s == 'perrin':
            a = 3
            b = 0
            c = 2
        else:
            a = 0
            b = 1
            c = 1
        i = 3
        while True:
            n = a + b
            if s == 'tribonacci':
                n += c
            if i == u:
                return n
            a = b
            b = c
            c = n
            i += 1
    else:
        if s == 'lucas':
            a = 2
        else:
            a = 0
        b = 1
        i = 2
        while True:
            n = a + b
            if s == 'pell':
                n += b
            elif s == 'jacobsthal':
                n += a
            if i == u:
                return n
            a = b
            b = n
            i += 1