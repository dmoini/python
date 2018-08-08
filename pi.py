from decimal import Decimal
from decimal import getcontext
import math

# https://en.wikipedia.org/wiki/Chudnovsky_algorithm
def chudnovskyPi(precision):
    pi = Decimal(0)
    k = 0
    while k < precision:
        M = Decimal(math.factorial(6 * k)) / (Decimal(math.factorial(3 * k)) * Decimal(math.factorial(k)**3))
        L = Decimal((545140134 * k) + 13591409)
        X = Decimal(-262537412640768000**k)
        pi += (M * L) / X
        k += 1
    pi = pi**(-1)
    pi *= Decimal(426880) * Decimal(10005).sqrt()
    return pi * -1

def pi(precision):
    if precision > 100:
        print("This only goes up to 100 digits. Please input a new precision that is less than 100.")
    else:
        getcontext().prec = precision
        print(chudnovskyPi(precision))


precision = int(input("How many digits of pi would you like to compute? (100 max): "))
pi(precision)
