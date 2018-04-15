import math
#from math import sqrt

def kwadratowe(a, b, c):
    delta = b*b - 4*a*c
    if delta < 0:
        return ['Brak rozwiązań']
    elif delta == 0:
        return [-b/(2*a)]
    else:
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
        return [x1, x2]

#argument domyślny
def f(a=0):
    pass #null operation, nie robi nic

print(kwadratowe(2,4,2))