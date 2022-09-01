# Problem No.: 3295
# Solver:      Jinmin Goh
# Date:        20220901
# URL: https://www.acmicpc.net/problem/3295

import sys

def solve(graph, parent, visited, curr):
    visited[curr] = True
    for next in graph[curr]:
        if parent[next] == -1 or (not visited[parent[next]] and solve(graph, parent, visited, parent[next])):
            parent[next] = curr
            return 1
    return 0

def main():
    t = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        graph = [[] for _ in range(n)]
        for _ in range(m):
            a, b = map(int, sys.stdin.readline().split())
            graph[a].append(b)
        parent = [-1 for _ in range(n + 1)]
        ans = 0
        for i in range(n):
            visited = [False for _ in range(n + 1)]
            ans += solve(graph, parent, visited, i)
        print(ans)
    return

if __name__ == "__main__":
    main()