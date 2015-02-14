#coding=utf8
__author__ = '璐'

from datetime import date


def checkio(from_date, to_date):
    """
        Count the days of rest
    """
    count = 0
    if from_date.isoweekday() > 5:
        count = count + 7-from_date.isoweekday()+1
    if to_date.isoweekday() > 5:
        count = count + 7 - to_date.isoweekday() +1



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"

