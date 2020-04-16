# Problem No.: 11660
# Solver:      Jinmin Goh
# Date:        20200416
# URL: https://www.acmicpc.net/problem/11660

import sys

def main():
    n, m = map(int, input().split())
    table = []
    for _ in range(n):
        table.append(list(map(int, sys.stdin.readline().split())))
    dpTable = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if j == 0:
                dpTable[i][j] = table[i][j]
            else:
                dpTable[i][j] = dpTable[i][j - 1] + table[i][j]
    for i in range(1, n):
        for j in range(n):
            dpTable[i][j] += dpTable[i - 1][j]
    #print(dpTable)
    for _ in range(m):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        ans = 0
        if x1 == 1 and y1 == 1:
            ans = dpTable[x2 - 1][y2 - 1]
        elif x1 == 1:
            ans = dpTable[x2 - 1][y2 - 1] - dpTable[x2 - 1][y1 - 2]
        elif y1 == 1:
            ans = dpTable[x2 - 1][y2 - 1] - dpTable[x1 - 2][y2 - 1]
        else:
            ans = dpTable[x2 - 1][y2 - 1] - dpTable[x1 - 2][y2 - 1] - dpTable[x2 - 1][y1 - 2] + dpTable[x1 - 2][y1 - 2]
        print(ans)
    return

if __name__ == "__main__":
    main()