# Problem No.: 1761
# Solver:      Jinmin Goh
# Date:        20220722
# URL: https://www.acmicpc.net/problem/1761

import sys
sys.setrecursionlimit(10 ** 5)

def graph_construction(graph, depth, distance, ancestor, curr, parent):
    curr_w = 0
    for a, w in graph[parent]:
        if a == curr:
            curr_w = w
    depth[curr] = depth[parent] + 1
    distance[curr] = distance[parent] + curr_w
    ancestor[curr][0] = parent
    for i in range(1, 20):
        temp = ancestor[curr][i - 1]
        ancestor[curr][i] = ancestor[temp][i - 1]
    for next, w in graph[curr]:
        if next != parent:
            graph_construction(graph, depth, distance, ancestor, next, curr)

def main():
    # graph parsing
    n = int(sys.stdin.readline().rstrip())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, w = map(int, sys.stdin.readline().split())
        graph[a].append((b, w))
        graph[b].append((a, w))
    graph[0].append((1, 0))
    distance = [0 for _ in range(n + 1)]
    distance[0] = 0
    depth = [0 for _ in range(n + 1)]
    depth[0] = -1
    ancestor = [[0 for _ in range(20)] for _ in range(n + 1)]
    graph_construction(graph, depth, distance, ancestor, 1, 0)
    # query parsing
    m = int(sys.stdin.readline().rstrip())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        temp_a, temp_b = a, b
        if depth[temp_a] != depth[temp_b]:
            if depth[temp_a] > depth[temp_b]:
                temp_a, temp_b = temp_b, temp_a
            for i in reversed(range(20)):
                if depth[temp_a] <= depth[ancestor[temp_b][i]]:
                    temp_b = ancestor[temp_b][i]
        lca = temp_a
        if temp_a != temp_b:
            for i in reversed(range(20)):
                if ancestor[temp_a][i] != ancestor[temp_b][i]:
                    temp_a = ancestor[temp_a][i]
                    temp_b = ancestor[temp_b][i]
                lca = ancestor[temp_a][i]
        ans = distance[a] + distance[b] - 2 * distance[lca]
        print(ans)
    return

if __name__ == "__main__":
    main()