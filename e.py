from decimal import Decimal
from decimal import getcontext
import math

def brothers_e():
    e = 0
    n = 0
    while n <= 10:
        e += Decimal((2 * n) + 2) / Decimal(math.factorial((2 * n) + 1))
        n += 1
    return e

def calculate_e(precision):
    if precision > 100:
        print("This only goes up to 100 digits. Please input a new precision that is less than 100.")
    else:
        getcontext().prec = precision
        print(brothers_e())


precision = int(input("How many digits of pi would you like to compute? (100 max): "))
calculate_e(precision)
