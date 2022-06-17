# Problem No.: 11438
# Solver:      Jinmin Goh
# Date:        20220617
# URL: https://www.acmicpc.net/problem/11438

import sys
from math import log2

sys.setrecursionlimit(10 ** 5)

# dp table construncting function
def dp(graph, depth, ancestor, current, parent):
    depth[current] = depth[parent] + 1
    ancestor[current][0] = parent
    max_level = int(log2(10 ** 5 + 1))
    for i in range(1, max_level + 1):
        temp = ancestor[current][i - 1]     # temp: current's 2 ** (i - 1) th ancestor
        ancestor[current][i] = ancestor[temp][i - 1]    # current's 2 ** i th ancestor is same with current's 2 ** (i - 1) th ancestor's 2 ** (i - 1) th ancestor
    # dfs
    for node in graph[current]:
        if node != parent:
            dp(graph, depth, ancestor, node, current)
    return

def main():
    n = int(input())
    graph = {}
    # graph construction
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
        if b not in graph:
            graph[b] = []
        graph[b].append(a)
    # get query
    m = int(input())
    query = []
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        query.append((a, b))
    
    # dp table construction
    depth = [0 for _ in range(n + 1)]
    depth[0] = -1
    ancestor = [[0 for _ in range(20)] for __ in range(n + 1)]
    dp(graph, depth, ancestor, 1, 0)
    
    # query loop
    for (a, b) in query:
        # set depth of a and b same
        if depth[a] != depth[b]:
            if depth[a] > depth[b]:
                a, b = b, a
            for i in range(int(log2(10 ** 5 + 1)), -1, -1):
                # if b's 2 ** i th ancestor's depth is bigger than a's depth, keep go up
                if depth[a] <= depth[ancestor[b][i]]:
                    b = ancestor[b][i]
        # find LCA
        lca = a
        if a != b:
            for i in range(int(log2(10 ** 5 + 1)), -1, -1):
                if ancestor[a][i] != ancestor[b][i]:
                    a = ancestor[a][i]
                    b = ancestor[b][i]
                lca = ancestor[a][i]
        print(lca)
    return

if __name__ == "__main__":
    main()