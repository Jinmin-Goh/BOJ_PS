# Problem No.: 11022
# Solver:      Jinmin Goh
# Date:        191121
# URL: https://www.acmicpc.net/problem/11022

import sys

n = int(input())

for i in range(n):
    print(" " * (n - i - 1), end = "")
    print("*" * (i + 1))
