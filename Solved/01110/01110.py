# Problem No.: 1110
# Solver:      Jinmin Goh
# Date:        20191123
# URL: https://www.acmicpc.net/problem/1110

import sys

a = int(input())
temp1 = 0
temp2 = a
cnt = 0
while 1:
    cnt += 1
    temp1 = temp2 // 10 + temp2 % 10
    temp1 = temp1 % 10 + (temp2 % 10) * 10
    if temp1 == a:
        break
    temp2 = temp1

print(cnt)