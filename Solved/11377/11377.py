# Problem No.: 11377
# Solver:      Jinmin Goh
# Date:        20220825
# URL: https://www.acmicpc.net/problem/11377

import sys

def dfs(graph, visited, directed, curr):
    for next in graph[curr]:
        if visited[next]:
            continue
        visited[next] = True
        if directed[next] == -1 or dfs(graph, visited, directed, directed[next]):
            directed[next] = curr
            return True
    return False

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for i in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        for node in temp[1:]:
            graph[i + 1].append(node)
    ans = 0
    directed = [-1 for _ in range(m + 1)]
    for i in range(1, n + 1):
        visited = [False for _ in range(m + 1)]
        if dfs(graph, visited, directed, i):
            ans += 1
    cnt = 0
    for i in range(1, n + 1):
        visited = [False for _ in range(m + 1)]
        if dfs(graph, visited, directed, i):
            ans += 1
            cnt += 1
        if cnt == k:
            break
    print(ans)
    return

if __name__ == "__main__":
    main()