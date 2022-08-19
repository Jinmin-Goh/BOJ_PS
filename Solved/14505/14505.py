# Problem No.: 14505
# Solver:      Jinmin Goh
# Date:        20220819
# URL: https://www.acmicpc.net/problem/14505

import sys

def main():
    s = sys.stdin.readline().rstrip()
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 3
        else:
            dp[i][i + 1] = 2
    for i in range(2, n):
        for j in range(n - i):
            if s[j] != s[j + i]:
                dp[j][j + i] = dp[j][j + i - 1] + dp[j + 1][j + i] - dp[j + 1][j + i - 1]
            else:
                dp[j][j + i] = dp[j][j + i - 1] + dp[j + 1][j + i] + 1
    print(dp[0][n - 1])
    return

if __name__ == "__main__":
    main()