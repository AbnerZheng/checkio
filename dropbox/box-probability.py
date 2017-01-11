def checkio(marbles, step):
    def helper(white, s, current_pos, step):
        if step == 1:
            return 1.0*white / s * current_pos
        else:
            pos_l, pos_r = 0, 0
            if (white > 0):
                pos_l = helper(white - 1, s, current_pos * white / s, step - 1)
            if (white < s):
                pos_r = helper(white + 1, s, current_pos * (s - white) / s, step - 1)

            return pos_r + pos_l

    white = 0
    for e in marbles:
        if e == 'w':
            white += 1

    return round(helper(white,len(marbles),1.0,step),2)



# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u'bbw', 3) == 0.48, "1st example"
    assert checkio(u'wwb', 3) == 0.52, "2nd example"
    assert checkio(u'www', 3) == 0.56, "3rd example"
    assert checkio(u'bbbb', 1) == 0, "4th example"
    assert checkio(u'wwbb', 4) == 0.5, "5th example"
    assert checkio(u'bwbwbwb', 5) == 0.48, "6th example"
