# Problem No.: 13034
# Solver:      Jinmin Goh
# Date:        20220901
# URL: https://www.acmicpc.net/problem/13034

import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    dp = [0 for _ in range(n + 1)]
    dp[2] = 1
    for i in range(3, n + 1):
        visited = [False for _ in range(30)]
        j = 0
        while j <= i - 2 - j:
            visited[dp[j] ^ dp[i - 2 - j]] = True
            j += 1
        for j in range(30):
            if not visited[j]:
                dp[i] = j
                break
    print(1 if dp[n] else 2)
    return

if __name__ == "__main__":
    main()