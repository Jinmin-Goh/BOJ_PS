# Problem No.: 2673
# Solver:      Jinmin Goh
# Date:        20220825
# URL: https://www.acmicpc.net/problem/2673

import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    cost = [[0 for _ in range(101)] for _ in range(101)]
    for i in range(n):
        a, b = map(int, sys.stdin.readline().split())
        cost[a][b] = 1
        cost[b][a] = 1
    dp = [[0 for _ in range(101)] for _ in range(101)]
    for i in range(1, 101):
        for j in range(i, 0, -1):
            for k in range(j, i):
                dp[j][i] = max(dp[j][i], dp[j][k] + dp[k][i] + cost[j][i])
    print(dp[1][100])
    return

if __name__ == "__main__":
    main()