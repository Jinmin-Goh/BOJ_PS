# Problem No.: 2533
# Solver:      Jinmin Goh
# Date:        20220706
# URL: https://www.acmicpc.net/problem/2533

import sys

sys.setrecursionlimit(2000000)

def solve(graph, visited, y_dp, n_dp, i):
    if visited[i]:
        return
    visited[i] = True
    y_dp[i] = 1
    for node in graph[i]:
        if not visited[node]:
            solve(graph, visited, y_dp, n_dp, node)
            y_dp[i] += min(y_dp[node], n_dp[node])
            n_dp[i] += y_dp[node]

def main():
    n = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    y_dp = [0 for _ in range(n)]
    n_dp = [0 for _ in range(n)]
    visited = [False for _ in range(n)]
    solve(graph, visited, y_dp, n_dp, 0)
    print(min(y_dp[0], n_dp[0]))
    return

if __name__ == "__main__":
    main()