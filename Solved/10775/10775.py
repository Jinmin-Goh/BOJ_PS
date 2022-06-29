# Problem No.: 10775
# Solver:      Jinmin Goh
# Date:        20220629
# URL: https://www.acmicpc.net/problem/10775

import sys

def union(p, x, y):
    x = find(p, x)
    y = find(p, y)
    if x > y:
        p[x] = y
    elif x < y:
        p[y] = x

def find(p, x):
    if p[x] == -1:
        return -1
    elif p[x] == x:
        return x
    p[x] = find(p, p[x])
    return p[x]

def main():
    g = int(input())
    p = int(input())
    nums = [int(sys.stdin.readline().rstrip()) - 1 for _ in range(p)]
    parent = [-1 for _ in range(g)]
    ans = 0
    for i in nums:
        val = find(parent, i)
        if val == -1:
            parent[i] = i
            ans += 1
            if i > 0 and find(parent, i - 1) != -1:
                union(parent, i - 1, i)
            if i < g - 1 and find(parent, i + 1) != -1:
                union(parent, i, i + 1)
        elif val == 0:
            break
        else:
            ans += 1
            parent[val - 1] = val - 1
            parent[i] = val - 1
            if i - 1 > 0 and find(parent, val - 2) != -1:
                union(parent, val - 2, val - 1)
            if i - 1 < g - 1 and find(parent, val) != -1:
                union(parent, val - 1, val)
    print(ans)
    return

if __name__ == "__main__":
    main()