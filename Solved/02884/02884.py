# Problem No.: 02884
# Solver:      Jinmin Goh
# Date:        191120
# URL: https://www.acmicpc.net/problem/2884

h, m = input().split()

h = int(h)
m = int(m)

if m < 45:
    if h == 0:
        print(23, m + 15)
    else:
        print(h - 1, m + 15)
else:
    print(h, m - 45)