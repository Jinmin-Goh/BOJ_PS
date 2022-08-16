# Problem No.: 3648
# Solver:      Jinmin Goh
# Date:        20220812
# URL: https://www.acmicpc.net/problem/3648

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
    t = sys.stdin.readline().rstrip()
    while t:
        n, m = map(int, t.split())
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
        graph[0].append(1)
        rev_graph[1].append(0)
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
        flag = True
        for i in range(n):
            if group[i * 2] == group[i * 2 + 1]:
                print("no")
                flag = False
                break
        if flag:
            print("yes")
        t = sys.stdin.readline().rstrip()
    return

if __name__ == "__main__":
    main()