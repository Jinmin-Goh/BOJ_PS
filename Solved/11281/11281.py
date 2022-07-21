# Problem No.: 11281
# Solver:      Jinmin Goh
# Date:        20220721
# URL: https://www.acmicpc.net/problem/11281

import sys

sys.setrecursionlimit(10 ** 5)

def dfs(graph, visited, i, stack):
    if visited[i]:
        return
    visited[i] = True
    for node in graph[i]:
        if visited[node]:
            continue
        dfs(graph, visited, node, stack)
    stack.append(i)

def dfs2(graph, visited, i, stack):
    if visited[i]:
        return
    visited[i] = True
    stack.append(i)
    for node in graph[i]:
        if visited[node]:
            continue
        dfs2(graph, visited, node, stack)

def main():
    # input parsing
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(2 * n)]
    rev_graph = [[] for _ in range(2 * n)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        a = a * 2 - 1 if a > 0 else (-a - 1) * 2
        b = b * 2 - 1 if b > 0 else (-b - 1) * 2
        graph[a - 1 if a % 2 else a + 1].append(b)
        graph[b - 1 if b % 2 else b + 1].append(a)
        rev_graph[b].append(a - 1 if a % 2 else a + 1)
        rev_graph[a].append(b - 1 if b % 2 else b + 1)
    # get SCC
    stack = []
    visited = [False for _ in range(2 * n)]
    for i in range(2 * n):
        dfs(graph, visited, i, stack)
    visited = [False for _ in range(2 * n)]
    group = [-1 for _ in range(2 * n)]
    cnt = 0
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        temp = []
        dfs2(rev_graph, visited, node, temp)
        for i in temp:
            group[i] = cnt
        cnt += 1
    # check whether x and not x is in same SCC
    for i in range(n):
        if group[i * 2] == group[i * 2 + 1]:
            print(0)
            return
    print(1)
    # print proper values
    res = [-1 for _ in range(n)]
    scc_list = [(group[i], i) for i in range(2 * n)]
    scc_list.sort()
    for _, val in scc_list:
        if res[val // 2] == -1:
            res[val // 2] = 1 - (val % 2)
    for i in res:
        print(i, end=' ')
    return

if __name__ == "__main__":
    main()
    