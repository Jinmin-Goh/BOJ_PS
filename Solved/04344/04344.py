# Problem No.: 4344
# Solver:      Jinmin Goh
# Date:        20191128
# URL: https://www.acmicpc.net/problem/4344

import sys

n = int(input())
for i in range(n):
    std_score = input().split()
    std_cnt = int(std_score.pop(0))
    high_std_cnt = 0
    std_sum = 0
    for j in range(std_cnt):
        std_score[j] = int(std_score[j])
    for j in range(std_cnt):
        if std_score[j] > sum(std_score) / std_cnt:
            high_std_cnt += 1
    print("%0.3f" % float(round(high_std_cnt / std_cnt * 100, 3)), end="")
    print('%')
        