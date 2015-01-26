#coding=utf8
#http://www.checkio.org/mission/brackets/solve/
__author__ = '璐'

def checkio2(data):
    stack=[""]
    brackets={"(":")","[":"]","{":"}"}
    for c in data:
        if c in brackets:
            stack.append(brackets[c])
        elif c in brackets.values() and c!=stack.pop():
            return False
    return stack==[""]

def checkio(expression):
    open_brackets = ("{","[","(")
    close_brackets = ("}","]",")")
    stack = []
    for e in expression:
        if e in open_brackets:
            stack.append(e)
        elif e in close_brackets:
            if stack:
                if abs(ord(e) - ord(stack.pop())) < 3:
                    continue
                else:
                    return False
            else:
                return False
    return False if stack else True


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    checkio("[[[1+[1+1]]])")
