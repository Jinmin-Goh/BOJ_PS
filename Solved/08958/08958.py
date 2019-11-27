# Problem No.: 8958
# Solver:      Jinmin Goh
# Date:        20191128
# URL: https://www.acmicpc.net/problem/8958

import sys

n = int(input())
sum = 0
for i in range(n):
    result = input()
    res_list = result.split('X')
    sum = 0
    for j in range(len(res_list)):
        for k in range(len(res_list[j])):
            sum += k + 1
    print(sum)