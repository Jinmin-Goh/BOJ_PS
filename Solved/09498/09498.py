# Problem No.: 09498
# Solver:      Jinmin Goh
# Date:        191120
# URL: https://www.acmicpc.net/problem/9498


a = input()

a = int(a)

if a >= 90:
    print("A")
elif a >= 80:
    print("B")
elif a >= 70:
    print("C")
elif a >= 60:
    print("D")
else:
    print("F")