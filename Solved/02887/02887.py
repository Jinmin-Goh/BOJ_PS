# Problem No.: 2887
# Solver:      Jinmin Goh
# Date:        20220701
# URL: https://www.acmicpc.net/problem/2887

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
    n = int(input())
    x_list = []
    y_list = []
    z_list = []
    for i in range(n):
        x, y, z = map(int, sys.stdin.readline().split())
        x_list.append((x, i))
        y_list.append((y, i))
        z_list.append((z, i))
    x_list.sort()
    y_list.sort()
    z_list.sort()
    weight = []
    for i in range(n - 1):
        weight.append((x_list[i + 1][0] - x_list[i][0], x_list[i][1], x_list[i + 1][1]))
        weight.append((y_list[i + 1][0] - y_list[i][0], y_list[i][1], y_list[i + 1][1]))
        weight.append((z_list[i + 1][0] - z_list[i][0], z_list[i][1], z_list[i + 1][1]))
    weight.sort()
    parent = [i for i in range(n)]
    ans = 0
    cnt = 0
    for w, a, b in weight:
        if find(parent, a) == find(parent, b):
            continue
        ans += w
        cnt += 1
        union(parent, a, b)
        if cnt == n - 1:
            break
    print(ans)
        
    return

if __name__ == "__main__":
    main()