# Problem No.: 11727
# Solver:      Jinmin Goh
# Date:        20200310
# URL: https://www.acmicpc.net/problem/11727

import sys

def main():
    n = int(input())
    if n == 1:
        print(1)
        return
    if n == 2:
        print(3)
        return
    dpList = [0] * (n + 1)
    dpList[1] = 1
    dpList[2] = 3
    for i in range(3, n + 1):
        dpList[i] = (dpList[i - 1] + 2 * dpList[i - 2]) % 10007
    print(dpList[-1])
    return

if __name__ == "__main__":
    main()