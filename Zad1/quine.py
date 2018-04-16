import expression

class Minterm:
    def __init__(self, t = "", n = [], i = 0):
        self.term = t
        self.num = n
        self.ind = i

    def setMinterm(self, t, n, i):
        self.term = t
        self.num = n
        self.ind = i

    def setInd(self, i):
        self.ind = i
        return self

    def getMinterm(self):
        return self.term

    def getMintermNum(self):
        return self.num

    def getMintermInd(self):
        return self.ind

    def __str__(self):
        return self.term

    def __repr__(self):
        return str(self.ind) + ": " + str(self.num) + ": " + self.term

    def __eq__(self, other):
        return self.term == other.term

    def oneDiffer(self, other): #checks if two minterms differ only on one bit
        c = 0
        i = 0
        while i < len(self.term):
            if self.term[i] != other.term[i]:
                c += 1
            i += 1
        return c == 1

    def replaceInvital(self, other): #replaces non-essential bits in given minterms
        i = 0
        n = ""
        while i < len(self.term):
            if self.term[i] != other.term[i]:
                n += "-"
            else:
                n += self.term[i]
            i += 1
        t = []
        t.extend(self.num)
        t.extend(other.num)
        return Minterm(n, t)

class Term:
    def __init__(self, i):
        self.ind = i
        self.set = [] #set of minterms which crossed this Term

    def addToSet(self, s):
        self.set.append(s)

    def multiplySet(self, other):
        n = Term(self.ind)
        ni = []
        for x in self.set:
            for sx in other.set:
                for sxi in sx:
                    ni = set(x)
                    if sxi not in x:  
                        ni.add(sxi)
                n.set.append(ni) 
        return n
    
    def deleteSame(self):
        i = 0
        while i < len(self.set):
            j = i + 1
            while j < len(self.set):
                if self.set[i].issubset(self.set[j]):
                    del self.set[j]
                    j -= 1
                elif self.set[j].issubset(self.set[i]):
                    del self.set[i]
                    j -= 1
                    i -= 1
                j += 1
            i += 1

class Func:
    def __init__(self, expr):
        self.Minterms = self.makeMinterms(expr)
        self.Terms = self.getIndexes()
        self.Variables = expression.getVariables(expr)

    def reduceTerms(self):
        if len(self.Terms) < 2:
            return
        while len(self.Terms) != 1:
            self.Terms[0] = self.Terms[0].multiplySet(self.Terms[1])
            self.Terms[0].deleteSame()
            del self.Terms[1]

    def retIngredient(self, i):
        s = "("
        for n, el in enumerate(self.Minterms[i].term):
            if el == '1':
                s += self.Variables[n] + " & "
            if el == '0':
                s += '!' + self.Variables[n] + " & "
        return s[0:len(s)-3] + ")"

    def printResult(self):
        s = ""
        for el in self.Terms[0].set[0]:
            s += self.retIngredient(el) + " | "
        if s[0:len(s)-3] != ")":
            print(s[0:len(s)-3])
        else:
            print("1")

    def getIndexes(self):
        t = []
        for el in self.Minterms:
            t.append(Term(el.num[0]))
        return t

    def setSets(self):
        for el in self.Terms:
            for t in self.Minterms:
                if el.ind in t.num:
                    el.addToSet(set([t.ind]))

    def showTerms(self):
        for el in self.Terms:
            print("Set: " + str(el.ind) + ": " + str(el.set))
    
    def makeMinterms(self, expr): #getting expression in RPN
        Minterms = []
        vars = expression.getVariables(expr)
        for x in range(0, 2**len(vars)):
            perm = bin(x)
            perm = perm[2:]
            perm = perm.rjust(len(vars), '0')
            if expression.evaluate(expression.insertValues(expr, vars, perm)) == "1":
                Minterms.append(Minterm(perm, [x], len(Minterms)))
        return Minterms

    def reduceStep(self, minterms): #reduces given minterms to minimum
        i = 0
        j = 0
        newMinterms = []
        checked = []

        while i < len(minterms):
            checked.append(0)
            i += 1

        i = 0
        while i < len(minterms):
            j = i
            while j < len(minterms):
                if minterms[i].oneDiffer(minterms[j]):
                    if minterms[i].replaceInvital(minterms[j]) not in newMinterms:
                        newMinterms.append(minterms[i].replaceInvital(minterms[j]).setInd(len(newMinterms)))
                    checked[i] = 1
                    checked[j] = 1
                j += 1
            i += 1
        i = 0
        while i < len(minterms):
            if checked[i] != 1 and minterms[i] not in newMinterms:
                newMinterms.append(minterms[i].setInd(len(newMinterms)))
            i += 1
        return newMinterms

    def reduce(self):
        newTerms = self.Minterms
        while(newTerms != self.reduceStep(newTerms)):
            newTerms = self.reduceStep(newTerms)
        self.Minterms = newTerms

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
            func = Func(expr)
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

