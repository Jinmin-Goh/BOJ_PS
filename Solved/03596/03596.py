# Problem No.: 3596
# Solver:      Jinmin Goh
# Date:        20220901
# URL: https://www.acmicpc.net/problem/3596

import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    dp = [0 for _ in range(2001)]
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4, 2001):
        visited = [False for _ in range(2000)]
        j = 1
        while j <= (i + 1) // 2:
            temp = dp[i - j - 2] ^ (dp[j - 3] if j - 3 > 0 else 0)
            visited[temp] = True
            j += 1
        for j in range(2000):
            if not visited[j]:
                dp[i] = j
                break
    print(1 if dp[n] else 2)
    return

if __name__ == "__main__":
    main()