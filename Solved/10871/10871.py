# Problem No.: 10871
# Solver:      Jinmin Goh
# Date:        191121
# URL: https://www.acmicpc.net/problem/10871

import sys

n, x = input().split()
n = int(n)
x = int(x)
a = input().split()
ans = []
for i in range(len(a)):
    a[i] = int(a[i])
    if a[i] < x:
        ans.append(a[i])

for i in range(len(ans)):
    print(ans[i], end = " ")