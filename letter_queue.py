#coding=utf8
__author__ = '璐'

def letter_queue(commands):
    import collections
    queue = collections.deque()
    for command in commands:
        if command.startswith("PUSH"):
            queue.append(command[-1])
        elif queue:
            queue.popleft()
    return "".join(queue)

def letter_queue_self(commands):
    result = []
    for c in commands:
        if c.startswith("PUSH"):
            result.insert(0,c.split()[1])
        else:
            if result:
                result.pop()
    result.reverse()
    return "".join(result)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"

