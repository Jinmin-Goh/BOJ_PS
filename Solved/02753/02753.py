# Problem No.: 02753
# Solver:      Jinmin Goh
# Date:        191120
# URL: https://www.acmicpc.net/problem/2753

a = input()

a = int(a)

if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)