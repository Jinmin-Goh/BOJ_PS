# Problem No.: 2169
# Solver:      Jinmin Goh
# Date:        20220721
# URL: https://www.acmicpc.net/problem/2169

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    table = [list(map(int, sys.stdin.readline().split())) for _  in range(n)]
    dp = [[[-1000000000, -1000000000, -1000000000] for _ in range(m)] for _ in range(n)]
    dp[0][0] = [table[0][0], table[0][0], table[0][0]]
    for i in range(1, m):
        for j in range(3):
            dp[0][i][j] = dp[0][i - 1][j] + table[0][i]
    for i in range(1, n):
        dp[i][0][1] = dp[i - 1][0][0] + table[i][0]
        for j in range(1, m):
            val = max(dp[i - 1][j][0], dp[i][j - 1][1]) + table[i][j]
            dp[i][j][1] = max(dp[i][j][1], val)
        dp[i][m - 1][2] = dp[i - 1][m - 1][0] + table[i][m - 1]
        for j in reversed(range(m - 1)):
            val = max(dp[i - 1][j][0], dp[i][j + 1][2]) + table[i][j]
            dp[i][j][2] = max(dp[i][j][2], val)
        for j in range(m):
            dp[i][j][0] = max(dp[i][j][1], dp[i][j][2])
        
    print(max(dp[-1][-1]))
    return

if __name__ == "__main__":
    main()