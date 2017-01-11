#coding=utf8
# 主要难点就在于括号的处理
def parse_molecule(formula):
    def consume(f):
        return (f[0], f[1:])

    def deale(head, formula, result):
        while len(formula):
            (head, formula) = consume(formula)
            if(head in param_pairs.values()):
                formula = head + formula
                break
            if head in param_pairs:
                (r, formula) = helper(head, formula, {})  # 处理括号
                for e in r:
                    if e in result:
                        result[e] += r[e]
                    else:
                        result[e] = r[e]
            elif head.isupper():  # 大写字母
                name = head
                while (len(formula) and formula[0].islower()):
                    name += formula[0]
                    formula = formula[1:]
                if (len(formula) and formula[0].isdigit()):
                    multi = formula[0]
                    formula = formula[1:]
                    while (len(formula) and formula[0].isdigit()):
                        multi += formula[0]
                        formula = formula[1:]
                    multi = int(multi)
                else:
                    multi = 1
                if name in result:
                    result[name] = result[name] + multi
                else:
                    result[name] = multi
        return (result, formula)

    def helper(lParam, formula, result):
        (r, formula) = deale('', formula, {})
        (head, formula) = consume(formula)
        multi = 1
        if (head == param_pairs[lParam]):
            # 括号匹配
            if (formula[0].isdigit()):
                multi = formula[0]
                formula = formula[1:]
                while len(formula) and formula[0].isdigit():
                    multi += formula[0]
                    formula = formula[1:]
                multi = int(multi)
            else:
                multi = 1
        for e in r:
            if e in result:
                result[e] += r[e] * multi
            else:
                result[e] = r[e] * multi
        return (result, formula)

    param_pairs = {'(': ')', '[': ']', '{': '}'}  # param = param_pairs.keys()


    return deale('', formula, {})[0]


def equals_atomically(obj1, obj2):
    if len(obj1) != len(obj2):
        return False
    for k in obj1:
        if obj1[k] != obj2[k]:
            return False
    return True


# print parse_molecule("H2O")
print parse_molecule("Mg(OH)2")

print equals_atomically(parse_molecule("H2O"), {'H': 2, 'O': 1})
print equals_atomically(parse_molecule("Mg(OH)2"), {'Mg': 1, 'O': 2, 'H': 2})
print equals_atomically(parse_molecule("K4[ON(SO3)2]2"), {'K': 4, 'O': 14, 'N': 2, 'S': 4})
