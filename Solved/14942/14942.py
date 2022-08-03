# Problem No.: 14942
# Solver:      Jinmin Goh
# Date:        20220803
# URL: https://www.acmicpc.net/problem/14942

import sys

def construct(graph, ancestor, curr, parent):
    weight = 0
    for node, w in graph[curr]:
        if node == parent:
            weight = w
            break
    ancestor[curr][0] = (parent, weight)
    for i in range(1, 20):
        temp, temp_w = ancestor[curr][i - 1]
        ancestor[curr][i] = (ancestor[temp][i - 1][0], ancestor[temp][i - 1][1] + temp_w)
    for next, _ in graph[curr]:
        if next != parent:
            construct(graph, ancestor, next, curr)

def main():
    n = int(sys.stdin.readline().rstrip())
    energy = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    energy = [0] + energy
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, w = map(int, sys.stdin.readline().split())
        graph[a].append((b, w))
        graph[b].append((a, w))
    graph[1].append((1, 10000000000))
    ancestor = [[(0, 10000000000) for _ in range(20)] for _ in range(n + 1)]
    construct(graph, ancestor, 1, 1)
    for node in range(1, n + 1):
        curr = node
        for i in reversed(range(20)):
            if energy[node] >= ancestor[curr][i][1]:
                energy[node] -= ancestor[curr][i][1]
                curr = ancestor[curr][i][0]
        print(curr)
    return

if __name__ == "__main__":
    main()