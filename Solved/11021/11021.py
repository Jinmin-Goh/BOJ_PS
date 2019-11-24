# Problem No.: 11021
# Solver:      Jinmin Goh
# Date:        191121
# URL: https://www.acmicpc.net/problem/11021

import sys

n = int(input())

for i in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    a = int(a)
    b = int(b)
    print("Case #" + str(i+1) + ": " + str(a + b))