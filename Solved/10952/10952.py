# Problem No.: 10952
# Solver:      Jinmin Goh
# Date:        191121
# URL: https://www.acmicpc.net/problem/10952

import sys

while 1:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a == 0 and b == 0:
        break
    print(a + b)
