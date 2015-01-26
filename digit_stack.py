#coding=utf8
__author__ = '璐'

def digit_stack(commands):
    sum = 0
    stack = []
    for c in commands:
        if "PUSH" in c:
            value = int(c.split()[1])
            stack.append(value)
        elif "POP" in c:
            if stack:
                sum+=stack.pop()
            else:
                sum+=0
        else:
            if stack:
                sum+=stack[-1]
            else:
                sum+=0
    return sum




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"

