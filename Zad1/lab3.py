#Dodawanie wielomianów"

class Wielomian:
    d = {}
    def __init__(self):
        self.d = {}
    
    def dodajJednomian(self, wyk, wsp):
        if wyk in self.d:
            self.d[wyk] = self.d[wyk] + wsp
        else:
            self.d[wyk] = wsp

    def wypisz(self):
        s = ""
        for el in self.d:
            s += str(self.d[el]) + "x^" + str(el) + " + "
        print(s[0:(len(s)-3)])

    def __add__(self, other):
        n = Wielomian()
        n = self.d.update(other.d)
        '''for el in other.d:
            if el in self.d:
                n.d[el] = self.d[el] + other.d[el]
            else:
                n.d[el] = other.d[el]'''
        return n

    def __iadd__(self, other):
        self.d.update(other.d)
        '''for el in other.d:
            if el in self.d:
                self.d[el] += other.d[el]
            else:
                self.d[el] = other.d[el]'''
        return self


w = Wielomian()
x = Wielomian()
z = Wielomian()
x.dodajJednomian(3, 1)
x.dodajJednomian(2, 5)
w.dodajJednomian(1, 2)
w.dodajJednomian(2, 3)
z = x + w
w += x
w.wypisz()
x.wypisz()
z.wypisz()