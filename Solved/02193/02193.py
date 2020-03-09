# Problem No.: 2193
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/2193

import sys

def main():
    n = int(input())
    if n == 1:
        print(1)
        return
    dpList = [[0] * 2 for i in range(n + 1)]
    dpList[1] = [0, 1]
    for i in range(2, n + 1):
        dpList[i][0] = sum(dpList[i - 1])
        dpList[i][1] = dpList[i - 1][0]
    print(sum(dpList[-1]))
    return

if __name__ == "__main__":
    main()