# Problem No.: 10818
# Solver:      Jinmin Goh
# Date:        20191125
# URL: https://www.acmicpc.net/problem/10818

import sys

a = int(input())
num = input().split()

for i in range(len(num)):
    num[i] = int(num[i])

print(min(num), max(num))