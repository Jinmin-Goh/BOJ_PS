# Problem No.: 2577
# Solver:      Jinmin Goh
# Date:        20191127
# URL: https://www.acmicpc.net/problem/2577

import sys

a = int(input())
b = int(input())
c = int(input())
num = a * b * c
count = [0,0,0,0,0,0,0,0,0,0]

while num != 0:
    count[num % 10] += 1
    num = num // 10

for i in range(10):
    print(count[i])