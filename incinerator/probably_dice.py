# 这题就是简单的动态规划
# count(dice_number, sides, target) = count(dice_number-1, sides, target - i) for i in 1..(sides+1)
# 使用一层就可以
def probability(dice_number, sides, target):
    cl = [1 if 0< e <= sides else 0 for e in range(target + 1)]
    for ee in range(dice_number-1):
        for e in range(target, 0 , -1):
            cl[e] = sum([cl[e-1-i] if e-1-i>0 else 0 for i in range(sides)])
    result = round(cl[target] / sides**dice_number, 4)
    return result



if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision


    assert (almost_equal(probability(1, 2, 0), 0)), "Basic example"
    assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
