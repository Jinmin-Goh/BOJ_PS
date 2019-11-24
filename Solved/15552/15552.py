# Problem No.: 15552
# Solver:      Jinmin Goh
# Date:        191121
# URL: https://www.acmicpc.net/problem/15552

import sys

n = int(input())

for i in range(n):
    # fast version of input function
    a, b = sys.stdin.readline().rstrip().split()
    a = int(a)
    b = int(b)
    print(a + b)