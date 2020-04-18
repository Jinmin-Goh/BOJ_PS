# Problem No.: 9663
# Solver:      Jinmin Goh
# Date:        20200417
# URL: https://www.acmicpc.net/problem/9663

import sys

usedCol = []
usedRDiag = []
usedLDiag = []

def search(n: int, row: int) -> int:
    if row == n:
        return 1
    ans = 0
    for i in range(n):
        if i in usedCol:
            continue
        if row - i in usedRDiag:
            continue
        if row + i in usedLDiag:
            continue
        usedCol.append(i)
        usedRDiag.append(row - i)
        usedLDiag.append(row + i)
        ans += search(n, row + 1)
        usedCol.pop()
        usedRDiag.pop()
        usedLDiag.pop()
    return ans

def main():
    n = int(input())
    global usedCol
    global usedRDiag
    global usedLDiag
    ans = search(n, 0)
    print(ans)
    return

if __name__ == "__main__":
    main()