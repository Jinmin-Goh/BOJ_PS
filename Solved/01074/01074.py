# Problem No.: 1074
# Solver:      Jinmin Goh
# Date:        20200607
# URL: https://www.acmicpc.net/problem/1074

import sys

def main():
    n, row, col = map(int, input().split())
    length = 2 ** (n - 1)
    rowPos = 0
    colPos = 0
    ans = 0
    while length > 0:
        if rowPos + length <= row:
            ans += length * length * 2
            rowPos += length
        if colPos + length <= col:
            ans += length * length
            colPos += length
        #print(rowPos, colPos, length, ans)
        length = length // 2
    print(ans)
    return

if __name__ == "__main__":
    main()