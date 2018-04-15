import string

VARS = string.ascii_lowercase + string.ascii_uppercase + "0123456789"
OPS = ["&", "|", "<=>", "!", "=>", "xor"]

def validate(expr):
    """sprawdza poprawność syntaktyczną wyrażenia"""
    state = True  # True - oczekiwany nawias ( lub zmienna, False - oczekiwany nawias ) lub operator
    par_count = 0     # licznik nawiasów 
    for el in expr:
        if el == " ":
            continue
        if state:
            if isVariable(el) or el == "0" or el == "1": 
                state = False 
            elif el == "(":
                par_count += 1
            elif el == "!":
                continue
            else:
                return False
        else:
            if el in OPS: 
                state = True
            elif el == ")":
                par_count -= 1
            else:
                return False
        if par_count < 0: return False
    return par_count == 0 and not state  # poprawne wyrażenie musi kończyć sie stanem False i mieć zamknięte wszystkie nawiasy

def isVariable(x):
    for el in x:
        if el not in VARS:
            return False
    return True

def splitExpression(expr):
    expr = expr.replace(" ", "")
    expr = expr.replace("(", "(,")
    expr = expr.replace(")", ",)")
    expr = expr.replace("<=>", "*")
    ops = list(OPS)
    ops.remove("<=>")
    ops.append("*")
    for el in ops:
        expr = expr.replace(el, "," + el + ",")
    expr = expr.replace(",!", "!")
    expr = expr.replace("*", "<=>")
    return expr.split(",")

def delBrackets(expr):
    count = 0
    i = 0
    while i < len(expr) - 2:
        i += 1
        if expr[i] == "(":
            count += 1
        elif expr[i] == ")":
            count -= 1
            if count < 0:
                return 0
        else:
            continue
    if count == 0:
        expr.pop(0)
        expr.pop()
        return 1
    else:
        return 0

def delOuterBrackets(expr):
    while expr[0] == "(" and expr[len(expr) - 1] == ")":
        if delBrackets(expr) == 0:
            return expr
    return expr

def variableAmount(expr):
    count = 0
    vars = []
    for el in expr:
        if el != "(" and el != ")" and el not in OPS and el not in vars:
            count += 1
            vars.append(el)
    return count

def priority(op):
    if op == "!":
        return 4
    elif op == "&":
        return 3
    elif op == "xor" or op == "|":
        return 2
    elif op == "<=>" or op == "=>":
        return 1
    else:
        return 0

def insertValues(expr, vars, perm):
    ret = list(expr)
    for ind, el in enumerate(ret):
        if el in vars:
            ret[ind] = perm[vars.index(el)]
    return ret

def getVariables(expr):
    vars = []
    for el in expr:
        if el != "(" and el != ")" and not el[0].isdigit() and el not in OPS and el not in vars:
            vars.append(el)
    return vars

def makeRPN(expr):
    stack = []
    RPN = []
    for el in expr:
        if el == "(":
            stack.append(el)
        elif el == ")":
            while stack[len(stack) - 1] != "(":
                RPN.append(stack.pop())
            stack.pop()
        elif el in OPS:
            if not stack or (priority(el) > priority(stack[len(stack) - 1])):
                stack.append(el)
            else:
                while stack and priority(el) < 4 and ((el != "=>" and priority(stack[len(stack) - 1]) >= priority(el)) or (el == "=>" and priority(stack[len(stack) - 1]) > priority(el))):
                    RPN.append(stack.pop())
                stack.append(el)
        else:
            RPN.append(el)
    while stack:
        RPN.append(stack.pop())
    return RPN

def operation(tmp1, tmp2, op):
    if op == "&":
        return tmp2 & tmp1
    elif op == "|":
        return tmp2 | tmp1
    elif op == "xor":
        if tmp1 == tmp2:
            return 0
        else:
            return 1
    elif op == "=>":
        if tmp2 == 1 and tmp1 == 0:
            return 0
        else:
            return 1
    elif op == "<=>":
        if tmp1 == tmp2:
            return 1
        else:
            return 0

def evaluate(expr):
    stack = []
    ops = list(OPS)
    ops.remove("!")
    for el in expr:
        if el == "!":
            tmp = int(stack.pop())
            if tmp == 0:
                tmp = 1
            else:
                tmp = 0
            stack.append(str(tmp))
        elif el in OPS:
            tmp1 = int(stack.pop())
            tmp2 = int(stack.pop())
            stack.append(str(operation(tmp1, tmp2, el)))
        else:
            stack.append(el)
    return stack[0]

def isTautology(expr):
    vars = getVariables(expr)
    for x in range(0, 2**len(vars)):
        perm = bin(x)
        perm = perm[2:]
        perm = perm.rjust(len(vars), '0')
        if evaluate(insertValues(expr, vars, perm)) == "0":
            return False
    return True
