# Problem No.: 3052
# Solver:      Jinmin Goh
# Date:        20191128
# URL: https://www.acmicpc.net/problem/3052

import sys

num = []
for i in range(10):
    num.append(int(input()) % 42)

num = set(num)
print(len(num))