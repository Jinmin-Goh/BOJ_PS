# Problem No.: 3830
# Solver:      Jinmin Goh
# Date:        20220816
# URL: https://www.acmicpc.net/problem/3830

import sys
sys.setrecursionlimit(10 ** 5)

def union(p, d, x, y, w):
    x_root = find(p, d, x)
    y_root = find(p, d, y)
    if x_root == y_root:
        return
    p[x_root] = y_root
    d[x_root] = d[y] + w - d[x]
    return

def find(p, d, x):
    if p[x] == x:
        return x
    r = find(p, d, p[x])
    d[x] += d[p[x]]
    p[x] = r
    return p[x]

def main():
    n, m = map(int, sys.stdin.readline().split())
    while n != 0 and m != 0:
        parent = [i for i in range(n + 1)]
        distance = [0 for _ in range(n + 1)]
        for _ in range(m):
            query = list(sys.stdin.readline().split())
            if query[0] == '!':
                a, b, w = map(int, query[1:])
                union(parent, distance, a, b, w)
            elif query[0] == '?':
                a, b = map(int, query[1:])
                if find(parent, distance, a) != find(parent, distance, b):
                    print("UNKNOWN")
                else:
                    print(distance[a] - distance[b])
        n, m = map(int, sys.stdin.readline().split())
    return

if __name__ == "__main__":
    main()