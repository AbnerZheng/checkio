#coding=utf8
__author__ = '璐'

def check_connection(network, first, second):
    future = []
    visited = []
    future.append(first)
    while(future):
        node = future.pop()
        visited.append(node)
        for e in network:
            temp = ""
            if e.find(node) == 0: #说明node为起始
                temp = e[e.index("-")+1:]
            elif e.find(node) > 0:
                temp = e[0:e.index("-")]
            if temp != "":
                if temp not in visited:
                    future.append(temp)
                    if second in future:
                        return True
    return False

def check_connection2(network, first, second):
    groups = set()
    for pair in network:
        p = set(pair.split("-"))
        new = p #The group to be added to groups
        for g in groups.copy():
            if g & p: #If any of the two new friends have friends in an existing group
                new |= g
                groups.remove(g)
        groups.add(frozenset(new))
    return any(first in g and second in g for g in groups)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."



