# Problem No.: 16202
# Solver:      Jinmin Goh
# Date:        20220905
# URL: https://www.acmicpc.net/problem/16202

import sys

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x == y:
        return
    parent[x] = y
    return

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    graph = []
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph.append((i + 1, a, b))
    graph.sort()
    flag = False
    for p in range(k):
        if flag:
            print(0, end=' ')
            continue
        parent = [i for i in range(n + 1)]
        cnt = 0
        cost = 0
        for i in range(p, m):
            w, a, b = graph[i]
            if find(parent, a) == find(parent, b):
                continue
            union(parent, a, b)
            cost += w
            cnt += 1
            if cnt == n - 1:
                break
        if cnt == n - 1:
            print(cost, end=' ')
        else:
            print(0, end=' ')
            flag = True
    return

if __name__ == "__main__":
    main()