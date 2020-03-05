# Problem No.: 1463
# Solver:      Jinmin Goh
# Date:        20200305
# URL: https://www.acmicpc.net/problem/1463

import sys

def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    if n in (2,3):
        print(1)
        return

    dpList = [0] * (n + 1)
    dpList[1] = 0
    dpList[2] = 1
    dpList[3] = 1
    for i in range(4, n + 1):
        temp1 = n
        temp2 = n
        temp3 = n
        if i % 3 == 0:
            temp1 = dpList[i // 3]
        if i % 2 == 0:
            temp2 = dpList[i // 2]
        temp3 = dpList[i - 1]
        dpList[i] = min(temp1, temp2, temp3) + 1
    print(dpList[n])

if __name__ == "__main__":
    main()