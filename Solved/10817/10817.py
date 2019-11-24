# Problem No.: 10817
# Solver:      Jinmin Goh
# Date:        191120
# URL: https://www.acmicpc.net/problem/10817

a = input()
a = a.split()
for i in range(3):
    a[i] = int(a[i])

a.sort()
print(a[1])