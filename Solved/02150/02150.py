# Problem No.: 2150
# Solver:      Jinmin Goh
# Date:        20220711
# URL: https://www.acmicpc.net/problem/2150

import sys
sys.setrecursionlimit(10 ** 5 + 10)

def dfs(graph, visited, i, stack):
    if visited[i]:
        return
    visited[i] = True
    for node in graph[i]:
        if visited[node]:
            continue
        dfs(graph, visited, node, stack)
    stack.append(i)

def dfs2(graph, visited, i, ans):
    if visited[i]:
        return
    visited[i] = True
    ans.append(i)
    for node in graph[i]:
        if visited[node]:
            continue
        dfs2(graph, visited, node, ans)

def main():
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v)]
    reversed_graph = [[] for _ in range(v)]
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a - 1].append(b - 1)
        reversed_graph[b - 1].append(a - 1)
    stack = []
    visited = [False for _ in range(v)]
    for i in range(v):
        dfs(graph, visited, i, stack)
    visited = [False for _ in range(v)]
    ans = []
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        temp = []
        dfs2(reversed_graph, visited, node, temp)
        temp.sort()
        ans.append(temp)
    ans.sort()
    print(len(ans))
    for component in ans:
        for node in component:
            print(node + 1, end=' ')
        print(-1)
    return

if __name__ == "__main__":
    main()