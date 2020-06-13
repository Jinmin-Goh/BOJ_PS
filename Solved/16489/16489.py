# Problem No.: 16489
# Solver:      Jinmin Goh
# Date:        20200612
# URL: https://www.acmicpc.net/problem/16489

import sys
import math
import decimal

# must use decimal to make less error value for big input

def main():
    a, b, c = map(int, input().split())
    a = decimal.Decimal(a)
    b = decimal.Decimal(b)
    c = decimal.Decimal(c)

    # calculate cos of A, B, C; law of cosines, cosA = (a^2 - b^2 - c^2) / (2bc)
    cosA = decimal.Decimal(a ** 2 - b ** 2 - c ** 2) / decimal.Decimal(2 * b * c)
    cosB = decimal.Decimal(b ** 2 - c ** 2 - a ** 2) / decimal.Decimal(2 * c * a)
    cosC = decimal.Decimal(c ** 2 - a ** 2 - b ** 2) / decimal.Decimal(2 * a * b)

    mul = decimal.Decimal((a + b + c) * (-a + b + c) * (a - b + c) * (a + b - c))

    # area S; Heron's formula
    S = (mul ** decimal.Decimal(0.5)) / decimal.Decimal(4)

    # radius of curcumcircle R; R = a/2sinA
    R = a / (decimal.Decimal(2) * ((decimal.Decimal(1) - cosA ** decimal.Decimal(2)) ** decimal.Decimal(0.5)))

    # radius of incircle r; r = S/s, s = (a + b + c) / 2
    r = (mul ** decimal.Decimal(0.5)) / (decimal.Decimal(2) * (a + b + c))

    # distance between incenter and circumcenter d; Euler's triangle theorem
    d = (a ** decimal.Decimal(2) / (decimal.Decimal(4) * (decimal.Decimal(1) - cosA ** decimal.Decimal(2))) - a * (mul ** decimal.Decimal(0.5)) / (((1 - cosA ** decimal.Decimal(2)) ** decimal.Decimal(0.5)) * decimal.Decimal(2) * (a + b + c))) ** decimal.Decimal(0.5)

    # sum of OH k; len(OH) = RcosA
    k = R * (abs(cosA) + abs(cosB) + abs(cosC))

    print(S)
    print(R)
    print(r)
    print(d)
    print(k)

    return

if __name__ == "__main__":
    main()