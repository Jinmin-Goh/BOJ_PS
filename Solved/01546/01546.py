# Problem No.: 1546
# Solver:      Jinmin Goh
# Date:        20191128
# URL: https://www.acmicpc.net/problem/1546

import sys

num = int(input())
score = input().split()
sum = 0
max_val = 0
for i in range(num):
    score[i] = int(score[i])
    sum += score[i]

print(sum / max(score) * 100 / num)