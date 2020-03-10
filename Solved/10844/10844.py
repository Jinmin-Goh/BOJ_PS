# Problem No.: 10844
# Solver:      Jinmin Goh
# Date:        20200310
# URL: https://www.acmicpc.net/problem/10844

import sys

def main():
    n = int(input())
    dpTable = [[0] * 10 for i in range(n + 1)]
    dpTable[1] = [0] + [1] * 9
    for i in range(2, n + 1):
        dpTable[i][0] = dpTable[i - 1][1]
        for j in range(1, 9):
            dpTable[i][j] = (dpTable[i - 1][j - 1] + dpTable[i - 1][j + 1]) % 1000000000
        dpTable[i][9] = dpTable[i - 1][8]
    print(sum(dpTable[-1]) % 1000000000)
    return

if __name__ == "__main__":
    main()