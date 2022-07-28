# Problem No.: 11266
# Solver:      Jinmin Goh
# Date:        20220728
# URL: https://www.acmicpc.net/problem/11266

import sys

sys.setrecursionlimit(10 ** 5)

def dfs(graph, visited, cut, curr, num, root):
    visited[curr] = num
    num += 1
    ret = visited[curr]
    child = 0
    for next in graph[curr]:
        if visited[next]:
            ret = min(ret, visited[next])
            continue
        child += 1
        prev = dfs(graph, visited, cut, next, num, False)
        if not root and prev >= visited[curr]:
            cut[curr] = True
        ret = min(ret, prev)
    if root:
        cut[curr] = child >= 2
    return ret

def main():
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0 for _ in range(v + 1)]
    cut = [False for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, v + 1):
        if visited[i] == 0:
            dfs(graph, visited, cut, i, 1, True)
    cnt = 0
    for i in range(1, v + 1):
        if cut[i]:
            cnt += 1
    print(cnt)
    for i in range(1, v + 1):
        if cut[i]:
            print(i, end=' ')
    return

if __name__ == "__main__":
    main()