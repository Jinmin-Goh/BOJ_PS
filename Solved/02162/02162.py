# Problem No.: 2162
# Solver:      Jinmin Goh
# Date:        20220630
# URL: https://www.acmicpc.net/problem/2162

import sys

def CCW(x1, y1, x2, y2, x3, y3):
    val = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    if val > 0:
        return 1
    elif val < 0:
        return -1
    else:
        return 0

def union(parent, cnt, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x == y:
        return
    parent[x] = y
    cnt[y] += cnt[x]
    cnt[x] = 0
    return

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def main():
    n = int(input())
    lines = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    parent = [i for i in range(n)]
    cnt = [1 for _ in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            x1, y1, x2, y2 = lines[i]
            x3, y3, x4, y4 = lines[j]
            val1 = CCW(x1, y1, x2, y2, x3, y3) * CCW(x1, y1, x2, y2, x4, y4)
            val2 = CCW(x3, y3, x4, y4, x1, y1) * CCW(x3, y3, x4, y4, x2, y2)
            if val1 == 0 and val2 == 0:
                if (x1, y1) > (x2, y2):
                    x1, x2, y1, y2 = x2, x1, y2, y1
                if (x3, y3) > (x4, y4):
                    x3, x4, y3, y4 = x4, x3, y4, y3
                if (x1, y1) <= (x4, y4) and (x2, y2) >= (x3, y3):
                    union(parent, cnt, i, j)
            elif val1 <= 0 and val2 <= 0:
                union(parent, cnt, i, j)
    ans = 0
    for i in cnt:
        if i != 0:
            ans += 1
    print(ans)
    print(max(cnt))
    return

if __name__ == "__main__":
    main()