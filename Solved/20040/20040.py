# Problem No.: 20040
# Solver:      Jinmin Goh
# Date:        20220628
# URL: https://www.acmicpc.net/problem/20040

import sys
sys.setrecursionlimit(500010)

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
    return

def find(p, x):
    if p[x] == x:
        return x
    p[x] = find(p, p[x])
    return p[x]

def main():
    n, m = map(int, input().split())
    p = [i for i in range(n)]
    h = [0 for _ in range(n)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if find(p, a) == find(p, b):
            print(i + 1)
            return
        else:
            union(h, p, a, b)
    print(0)
    
    return

if __name__ == "__main__":
    main()