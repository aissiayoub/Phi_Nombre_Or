from decimal import *
from math import *

def Pi():

    P = 10000
    C = Decimal(4) / 1
    I = 1
    a = 10000
    getcontext().prec = a

    for i in range(P, 0, -1):
        z = Decimal(4) / (I+2)
        if i%2 == 0:
            z = z*(-1)
        C += z
        I += 2

    
    return C

def approchePhiAvecPi():

    a = 10000
    getcontext().prec = a

    Phi = Decimal(1 - 2*cos(3*Pi()/5))
    print(Decimal(Phi))
