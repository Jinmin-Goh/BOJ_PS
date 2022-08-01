# Problem No.: 1006
# Solver:      Jinmin Goh
# Date:        20220801
# URL: https://www.acmicpc.net/problem/1006

import sys

def main():
    t = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, w = map(int, sys.stdin.readline().split())
        ring = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
        ring[0] = [0] + ring[0]
        ring[1] = [0] + ring[1]
        if n == 1:
            print(2 - int(ring[0][1] + ring[1][1] <= w))
            continue
        ans = n * 10
        # all separated case
        dp = [[0 for _ in range(n + 1)] for _ in range(3)]
        dp[0][1] = 1
        dp[1][1] = 1
        dp[2][1] = 2 - int(ring[0][1] + ring[1][1] <= w)
        for i in range(2, n + 1):
            outer = 2 - int(ring[0][i] + ring[0][i - 1] <= w)
            inner = 2 - int(ring[1][i] + ring[1][i - 1] <= w)
            horizon = 2 - int(ring[0][i] + ring[1][i] <= w)
            dp[0][i] = min(dp[2][i - 1] + 1, dp[1][i - 1] + outer)
            dp[1][i] = min(dp[2][i - 1] + 1, dp[0][i - 1] + inner)
            dp[2][i] = min(dp[0][i] + 1, dp[1][i] + 1, dp[2][i - 1] + horizon, dp[2][i - 2] + outer + inner)
        ans = min(ans, dp[2][n])
        # outer attached case
        dp = [[0 for _ in range(n + 1)] for _ in range(3)]
        if ring[0][n] + ring[0][1] <= w:
            dp[0][1] = 1
            dp[1][1] = n * 10
            dp[2][0] = n * 10
            dp[2][1] = 2
            for i in range(2, n + 1):
                outer = 2 - int(ring[0][i] + ring[0][i - 1] <= w)
                inner = 2 - int(ring[1][i] + ring[1][i - 1] <= w)
                horizon = 2 - int(ring[0][i] + ring[1][i] <= w)
                dp[0][i] = min(dp[2][i - 1] + 1, dp[1][i - 1] + outer)
                dp[1][i] = min(dp[2][i - 1] + 1, dp[0][i - 1] + inner)
                dp[2][i] = min(dp[0][i] + 1, dp[1][i] + 1, dp[2][i - 1] + horizon, dp[2][i - 2] + outer + inner)
            ans = min(ans, dp[1][n])
        # inner attached case
        dp = [[0 for _ in range(n + 1)] for _ in range(3)]
        if ring[1][n] + ring[1][1] <= w:
            dp[0][1] = n * 10
            dp[1][1] = 1
            dp[2][0] = n * 10
            dp[2][1] = 2
            for i in range(2, n + 1):
                outer = 2 - int(ring[0][i] + ring[0][i - 1] <= w)
                inner = 2 - int(ring[1][i] + ring[1][i - 1] <= w)
                horizon = 2 - int(ring[0][i] + ring[1][i] <= w)
                dp[0][i] = min(dp[2][i - 1] + 1, dp[1][i - 1] + outer)
                dp[1][i] = min(dp[2][i - 1] + 1, dp[0][i - 1] + inner)
                dp[2][i] = min(dp[0][i] + 1, dp[1][i] + 1, dp[2][i - 1] + horizon, dp[2][i - 2] + outer + inner)
            ans = min(ans, dp[0][n])
        # both attached case
        dp = [[0 for _ in range(n + 1)] for _ in range(3)]
        if ring[0][n] + ring[0][1] <= w and ring[1][n] + ring[1][1] <= w:
            dp[0][1] = n * 10
            dp[1][1] = n * 10
            dp[2][0] = n * 10
            dp[2][1] = 2
            for i in range(2, n + 1):
                outer = 2 - int(ring[0][i] + ring[0][i - 1] <= w)
                inner = 2 - int(ring[1][i] + ring[1][i - 1] <= w)
                horizon = 2 - int(ring[0][i] + ring[1][i] <= w)
                dp[0][i] = min(dp[2][i - 1] + 1, dp[1][i - 1] + outer)
                dp[1][i] = min(dp[2][i - 1] + 1, dp[0][i - 1] + inner)
                dp[2][i] = min(dp[0][i] + 1, dp[1][i] + 1, dp[2][i - 1] + horizon, dp[2][i - 2] + outer + inner)
            ans = min(ans, dp[2][n - 1])
        print(ans)
    return

if __name__ == "__main__":
    main()