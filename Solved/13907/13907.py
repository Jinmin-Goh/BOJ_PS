# Problem No.: 13907
# Solver:      Jinmin Goh
# Date:        20220808
# URL: https://www.acmicpc.net/problem/13907

import sys

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    s, d = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, w = map(int, sys.stdin.readline().split())
        graph[a].append((b, w))
        graph[b].append((a, w))
    query = [int(sys.stdin.readline().rstrip()) for _ in range(k)]
    dp = [[10 ** 9 for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][s] = 0
    for i in range(n):
        for j in range(1, n + 1):
            if dp[i][j] == 10 ** 9:
                continue
            for node, w in graph[j]:
                dp[i + 1][node] = min(dp[i + 1][node], dp[i][j] + w)
    min_val = 10 ** 9
    for i in range(n):
        min_val = min(min_val, dp[i][d])
    print(min_val)
    for q in query:
        for i in range(n):
            dp[i][d] += i * q
        min_val = 10 ** 9
        for i in range(n):
            min_val = min(min_val, dp[i][d]) 
        print(min_val)
    return

if __name__ == "__main__":
    main()