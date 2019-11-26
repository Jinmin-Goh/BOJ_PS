# Problem No.: 2562
# Solver:      Jinmin Goh
# Date:        20191125
# URL: https://www.acmicpc.net/problem/2562

import sys

num = []
for i in range(9):
    num.append(int(input()))

print(max(num))
print(num.index(max(num)) + 1)