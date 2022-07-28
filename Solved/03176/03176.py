# Problem No.: 3176
# Solver:      Jinmin Goh
# Date:        20220728
# URL: https://www.acmicpc.net/problem/3176

import sys

sys.setrecursionlimit(10 ** 5)

def construction(graph, ancestor, depth, curr, parent):
    depth[curr] = depth[parent] + 1
    weight = 0
    for a, w in graph[curr]:
        if a == parent:
            weight = w
    ancestor[curr][0] = (parent, weight, weight)
    for i in range(1, 20):
        temp, min_val, max_val = ancestor[curr][i - 1]
        ancestor[curr][i] = (ancestor[temp][i - 1][0], min(min_val, ancestor[temp][i - 1][1]), max(max_val, ancestor[temp][i - 1][2]))
    for next, _ in graph[curr]:
        if next != parent:
            construction(graph, ancestor, depth, next, curr)

def main():
    n = int(sys.stdin.readline().rstrip())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, w = map(int, sys.stdin.readline().split())
        graph[a].append((b, w))
        graph[b].append((a, w))
    graph[0].append((1, 0))
    graph[1].append((0, 0))
    depth = [0 for _ in range(n + 1)]
    ancestor = [[(0, 10000000, 0) for _ in range(20)] for _ in range(n + 1)]
    depth[0] = -1
    construction(graph, ancestor, depth, 1, 0)
    k = int(sys.stdin.readline().rstrip())
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        min_val = 10000000
        max_val = 0
        if depth[a] != depth[b]:
            if depth[a] > depth[b]:
                a, b = b, a
            for i in reversed(range(20)):
                if depth[a] <= depth[ancestor[b][i][0]]:
                    min_val = min(min_val, ancestor[b][i][1])
                    max_val = max(max_val, ancestor[b][i][2])
                    b = ancestor[b][i][0]
        if a == b:
            print(min_val, max_val)
            continue
        if a != b:
            for i in reversed(range(20)):
                if ancestor[a][i][0] != ancestor[b][i][0]:
                    min_val = min(min_val, ancestor[a][i][1], ancestor[b][i][1])
                    max_val = max(max_val, ancestor[a][i][2], ancestor[b][i][2])
                    a = ancestor[a][i][0]
                    b = ancestor[b][i][0]
        min_val = min(min_val, ancestor[a][0][1], ancestor[b][0][1])
        max_val = max(max_val, ancestor[a][0][2], ancestor[b][0][2])
        print(min_val, max_val)
    return

if __name__ == "__main__":
    main()