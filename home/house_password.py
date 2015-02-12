__author__ = '璐'

def checkio(data):
    if len(data)<10:
        return False
    upper,small,digit = False,False,False
    for e in data:
        if e.isupper():
            upper = True
        elif e.islower():
            small = True
        elif e.isdigit():
            digit = True
    return upper and small and digit

#其他人的解法：
checkio = lambda x: (len(x) >9 and
                     not x.isdigit() and
                     not x.islower() and
                     not x.isupper() and
                     not x.isalpha())
#根据逻辑运算可以获得，在运算复杂度上，会比常规方法忙个常数倍






if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"

