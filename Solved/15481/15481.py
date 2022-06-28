# Problem No.: 15481
# Solver:      Jinmin Goh
# Date:        20220628
# URL: https://www.acmicpc.net/problem/15481

import sys
from math import log2
sys.setrecursionlimit(2 * (10 ** 5) + 10)

def union(h, p, x, y):
    x = find(p, x)
    y = find(p, y)
    if x == y:
        return
    if h[x] < h[y]:
        p[x] = y
    else:
        p[y] = x
        if h[x] == h[y]:
            h[x] += 1

def find(p, x):
    if p[x] == x:
        return x
    p[x] = find(p, p[x])
    return p[x]

def construct(graph, table, depth, curr, parent, parent_weight = 0):
    depth[curr] = depth[parent] + 1
    table[curr][0] = (parent, parent_weight)
    for i in range(1, int(log2(200001)) + 1):
        temp, max1 = table[curr][i - 1]
        p2i, max2 = table[temp][i - 1]
        table[curr][i] = (p2i, max(max1, max2))
    for i, w in graph[curr]:
        if i != parent:
            construct(graph, table, depth, i, curr, w)

def main():
    # input parsing
    n, m = map(int, input().split())
    graph = [[] for i in range(n + 1)]
    edges = []
    for i in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
        edges.append((w, u, v, i))
    # find MST with no restriction
    edges.sort()
    p = [i for i in range(n + 1)]
    h = [0 for _ in range(n + 1)]
    sum_val = 0
    MST_set = set()
    new_graph = [[] for _ in range(n + 1)]
    for w, u, v, i in edges:
        if find(p, u) == find(p, v):
            continue
        sum_val += w
        MST_set.add(i)
        union(h, p, u, v)
        new_graph[u].append((v, w))
        new_graph[v].append((u, w))
    # construct sparse table
    root_node = edges[0][1]
    table = [[0 for _ in range(20)] for __ in range(n + 1)]
    depth = [0 for _ in range(n + 1)]
    depth[0] = -1
    construct(new_graph, table, depth, root_node, root_node)
    # LCA
    ans = [-1 for _ in range(m)]
    for w, u, v, pos in edges:
        if pos in MST_set:
            ans[pos] = sum_val
        else:
            max_val = -1
            if depth[u] != depth[v]:
                if depth[u] > depth[v]:
                    u, v = v, u
                for i in range(int(log2(200001)), -1, -1):
                    if depth[u] <= depth[table[v][i][0]]:
                        max_val = max(max_val, table[v][i][1])
                        v = table[v][i][0]
            if u != v:
                for i in range(int(log2(200001)), -1, -1):
                    if table[u][i][0] != table[v][i][0]:
                        max_val = max(max_val, table[u][i][1])
                        max_val = max(max_val, table[v][i][1])
                        u = table[u][i][0]
                        v = table[v][i][0]
                max_val = max(max_val, table[u][0][1])
                max_val = max(max_val, table[v][0][1])
            ans[pos] = sum_val + w - max_val
    for i in ans:
        print(i)
    return

if __name__ == "__main__":
    main()