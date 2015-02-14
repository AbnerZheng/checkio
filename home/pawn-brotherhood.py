__author__ = '璐'

def safe_pawns(pawns):
    paws_index = set()
    for p in pawns:
        row = int(p[1]) -1
        col = ord(p[0]) - 97
        paws_index.add((row,col))
    count = 0
    for row, col in paws_index:
        if ((row-1,col+1) in paws_index) or ((row-1,col-1) in paws_index):
            count += 1

    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

