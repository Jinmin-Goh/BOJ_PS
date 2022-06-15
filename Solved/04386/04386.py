# Problem No.: 4386
# Solver:      Jinmin Goh
# Date:        20220615
# URL: https://www.acmicpc.net/problem/4386

import sys

root = [i for i in range(101)]

def union(x, y):
    x = find(x)
    y = find(y)
    root[x] = y
    return

def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]

def main():
    n = int(input())
    point = []
    for _ in range(n):
        x, y = map(float, input().split())
        point.append((x, y))
    graph = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            graph.append((((point[j][0] - point[i][0]) ** 2 + (point[j][1] - point[i][1]) ** 2) ** 0.5, i, j))
    graph.sort()
    ans = 0.0
    for edge in graph:
        if find(edge[1]) == find(edge[2]):
            continue
        union(edge[1], edge[2])
        ans += edge[0]
    print(f"{ans:.2f}")
    return

if __name__ == "__main__":
    main()