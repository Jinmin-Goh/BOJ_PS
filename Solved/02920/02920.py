# Problem No.: 2920
# Solver:      Jinmin Goh
# Date:        20191126
# URL: https://www.acmicpc.net/problem/2920

import sys

num = input().split()
for i in range(len(num)):
    num[i] = int(num[i])

ascFlag = True
desFlag = True

for i in range(1,8):
    if num[i] >= num[i-1]:
        desFlag = False
    if num[i] <= num[i-1]:
        ascFlag = False

if desFlag:
    print("descending")

if ascFlag:
    print("ascending")

if not desFlag and not ascFlag:
    print("mixed")