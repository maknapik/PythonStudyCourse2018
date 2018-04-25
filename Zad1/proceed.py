import expression
import quine

def proceed():
    print("NOT - !\nAND - &\nOR - |\nXOR - xor\nIMPLICATION - =>\nEQUIVALENCE - <=>")
    expr = input("Write expression: ")
    expr = expression.splitExpression(expr)
    expr = expression.delOuterBrackets(expr)
    if(expression.validate(expr)):
        expr = expression.makeRPN(expr)
        if(expression.isTautology(expr)):
            print("Expression is a tautology")
        else:
            func = quine.Func(expr)
            if len(func.Minterms) < 1:
                print("Result:\n0")
            else:
                print("Minterms: " + str(func.Minterms))
                func.reduce()
                print("Reduced minterms: " + str(func.Minterms))
                func.setSets()
                #func.showTerms()
                func.reduceTerms()
                print("Result:")
                func.printResult()
    else:
        print("Wrong expression")

proceed()

expr = "!a&b&!c&!d|a&!b&!c&!d|a&!b&!c&d|a&!b&c&!d|a&!b&c&d|a&b&!c&!d|a&b&c&!d|a&b&c&d"
expr = "!a&b&!c&!d => !a&b xor !b&c <=> d&a"
expr = "a=>b=>c=>d<=>(!d)"
expr = "abc!de|du"