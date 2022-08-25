# Problem No.: 1671
# Solver:      Jinmin Goh
# Date:        20220825
# URL: https://www.acmicpc.net/problem/1671

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
    n = int(sys.stdin.readline().rstrip())
    sharks = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    graph = [[] for _ in range(2 * n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            if sharks[i] == sharks[j]:
                graph[i].append(j)
            elif sharks[i][0] >= sharks[j][0] and sharks[i][1] >= sharks[j][1] and sharks[i][2] >= sharks[j][2]:
                graph[i].append(j)
            elif sharks[i][0] <= sharks[j][0] and sharks[i][1] <= sharks[j][1] and sharks[i][2] <= sharks[j][2]:
                graph[j].append(i)
    ans = 0
    directed = [-1 for _ in range(n)]
    for i in range(n):
        visited = [False for _ in range(n)]
        dfs(graph, visited, directed, i)
        visited = [False for _ in range(n)]
        dfs(graph, visited, directed, i)
    for i in range(n):
        if directed[i] == -1:
            ans += 1
    print(ans)
    return

if __name__ == "__main__":
    main()