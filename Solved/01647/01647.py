# Problem No.: 1647
# Solver:      Jinmin Goh
# Date:        20220614
# URL: https://www.acmicpc.net/problem/1647

import sys

root = [i for i in range(100001)]

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
    n, m = map(int, input().split())
    graph = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph.append((c, a, b))
    graph.sort()
    ans = 0
    maxVal = 0
    for edge in graph:
        if find(edge[1]) == find(edge[2]):
            continue
        union(edge[1], edge[2])
        ans += edge[0]
        maxVal = max(maxVal, edge[0])
    print(ans - maxVal)
    return

if __name__ == "__main__":
    main()