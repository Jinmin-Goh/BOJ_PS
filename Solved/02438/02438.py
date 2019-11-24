# Problem No.: 02438
# Solver:      Jinmin Goh
# Date:        191121
# URL: https://www.acmicpc.net/problem/2438

import sys

n = int(input())

for i in range(n):
    for j in range(i + 1):
        print("*", end = "")
    print("\n", end = "")