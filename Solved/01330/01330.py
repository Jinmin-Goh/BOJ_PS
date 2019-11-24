# Problem No.: 01330
# Solver:      Jinmin Goh
# Date:        191120
# URL: https://www.acmicpc.net/problem/1330


a, b = input().split()

a = int(a)
b = int(b)

if a > b:
    print(">")
elif a == b:
    print("==")
else:
    print("<")
