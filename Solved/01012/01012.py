# Problem No.: 1012
# Solver:      Jinmin Goh
# Date:        20200606
# URL: https://www.acmicpc.net/problem/1012

import sys

def main():
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        table = [[0] * m for __ in range(n)]
        for __ in range(k):
            y, x = map(int, sys.stdin.readline().split())
            table[x][y] = 1
        ans = 0
        for i in range(n):
            for j in range(m):
                if table[i][j] == 1:
                    ans += 1
                    stack = [[i, j]]
                    while stack:
                        x, y = stack.pop()
                        if table[x][y] == 0:
                            continue
                        table[x][y] = 0
                        if x > 0:
                            stack.append([x - 1, y])
                        if x < n - 1:
                            stack.append([x + 1, y])
                        if y > 0:
                            stack.append([x, y - 1])
                        if y < m - 1:
                            stack.append([x, y + 1])
        print(ans)
                            
    return

if __name__ == "__main__":
    main()