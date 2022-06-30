# Problem No.: 1509
# Solver:      Jinmin Goh
# Date:        20220630
# URL: https://www.acmicpc.net/problem/1509

import sys

sys.setrecursionlimit(10000)

# check palindrome for all s[i : j + 1]
def check(s, pal, i, j):
    if pal[i][j] == None:
        if j - i == 1:
            pal[i][j] = s[i] == s[j]
        else:
            pal[i][j] = (s[i] == s[j]) and check(s, pal, i + 1, j - 1)
    return pal[i][j]

# count minimum palindrome split at s[i:n]
def solve(dp, pal, i):
    n = len(dp)
    if i == n:
        return 0
    if dp[i] == 3000:
        for j in range(i, n):
            if pal[i][j]:
                dp[i] = min(dp[i], 1 + solve(dp, pal, j + 1))
    return dp[i]

def main():
    s = input()
    n = len(s)
    dp = [3000 for _ in range(n)]
    pal = [[None for _ in range(n)] for __ in range(n)]
    for i in range(n):
        pal[i][i] = True
    for i in range(n):
        for j in range(i, n):
            check(s, pal, i, j)
    ans = solve(dp, pal, 0)
    print(ans)
    
    # O(n^3) TLE solution
    """
    dp = [[3000 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(1, n):
        for j in range(n - i):
            flag = True
            for k in range((i + 1) // 2):
                if s[j + k] != s[j + i - k]:
                    flag = False
                    break
            if flag:
                dp[j][j + i] = 1
                continue
            for k in range(i):
                dp[j][j + i] = min(dp[j][j + i], dp[j][j + k] + dp[j + k + 1][j + i])
    print(dp[0][n - 1])
    """
    return

if __name__ == "__main__":
    main()