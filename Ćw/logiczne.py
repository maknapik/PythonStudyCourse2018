def isVariable(sign):
    if ord(sign) > 96 and ord(sign) < 124:
        return True
    return False
###########################################
def isOperator(sign):
    if sign == "&":
        return True
    elif sign == "|":
        return True
    elif sign == "=>":
        return True
    elif sign == "<=>":
        return True
    else:
        return False
###########################################
def getVariables(expr):
    variables = []
    for char in expr:
        if(isVariable(char)):
            variables.append(char)
    variables.sort()
    return variables
###########################################
def correct(ciag):
    zam = 0
    otw = 0
    index = 0
    balanced = True
    wasOperator = False
    wasVariable = False
    wasOpenBracket = False
    wasClosedBracket = False

    while index < len(ciag):
        if ciag[index] == "(":
            otw += 1
            wasOpenBracket = True
        elif ciag[index] == ")":
            zam += 1
            wasClosedBracket = True
        elif otw < zam:
            balanced = False
        elif ciag[index] == "&" or ciag[index] == "|":
            wasOperator = True
        elif ciag[index] == "=" and ciag[index + 1] != ">":
            print("Wrong Operator in expression")
            return False
        elif ciag[index] == "=" and ciag[index + 1] == ">":
            wasOperator = True
            index += 1
        elif ciag[index] == "<" and (ciag[index + 1] != "=" and ciag[index + 2] != ">"):
            print("Wrong Operator in expression")
            return False
        elif ciag[index] == "=" and ciag[index + 1] == "=" and ciag[index + 2] == ">":
            wasOperator = True
            index += 2
        index += 1
    if otw != zam:
        balanced = False

    return balanced
###########################################
print(correct("(p & q) | ((r & s) & (f | c))"))
print(getVariables("(p & q) | ((r & s) & (f | c))"))

