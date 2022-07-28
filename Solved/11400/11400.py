# Problem No.: 11400
# Solver:      Jinmin Goh
# Date:        20220728
# URL: https://www.acmicpc.net/problem/11400

import sys

sys.setrecursionlimit(10 ** 5)

def dfs(graph, visited, cut, curr, num, p):
    visited[curr] = num
    num += 1
    ret = visited[curr]
    for next in graph[curr]:
        if next == p:
            continue
        if visited[next]:
            ret = min(ret, visited[next])
            continue
        prev = dfs(graph, visited, cut, next, num, curr)
        if prev > visited[curr]:
            cut.append((curr, next) if curr < next else (next, curr))
        ret = min(ret, prev)
    return ret

def main():
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0 for _ in range(v + 1)]
    cut = []
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, v + 1):
        if visited[i] == 0:
            dfs(graph, visited, cut, i, 1, 0)
    cut.sort()
    print(len(cut))
    for a, b in cut:
        print(a, b)
    return

if __name__ == "__main__":
    main()