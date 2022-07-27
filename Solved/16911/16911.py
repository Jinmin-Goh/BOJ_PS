# Problem No.: 16911
# Solver:      Jinmin Goh
# Date:        20220727
# URL: https://www.acmicpc.net/problem/16911

import sys

def union(stack, parent, depth, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x == y:
        return 0
    if depth[x] < depth[y]:
        x, y = y, x
    parent[y] = x
    if depth[x] == depth[y]:
        depth[x] += 1
        stack.append((x, y, 1))
    else:
        stack.append((x, y, 0))
    return 1

def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def update(arr, ql, qr, l, r, n, e):
    if ql <= l and r <= qr:
        arr[n].append(e)
        return
    if qr < l or r < ql:
        return
    m = (l + r) // 2
    update(arr, ql, qr, l, m, 2 * n, e)
    update(arr, ql, qr, m + 1, r, 2 * n + 1, e)

def solve(stack, query, depth, arr, parent, l, r, n):
    cnt = 0
    for a, b in arr[n]:
        cnt += union(stack, parent, depth, a, b)
    if l == r:
        res = find(parent, query[l][0]) == find(parent, query[l][1])
        print(int(res))
        revert(stack, depth, parent, cnt)
        return
    m = (l + r) // 2
    solve(stack, query, depth, arr, parent, l, m, 2 * n)
    solve(stack, query, depth, arr, parent, m + 1, r, 2 * n + 1)
    revert(stack, depth, parent, cnt)

def revert(stack, depth, parent, cnt):
    while cnt:
        x, y, n = stack.pop()
        parent[y] = y
        if n == 1:
            depth[x] -= 1
        cnt -= 1

def main():
    n, m = map(int, sys.stdin.readline().split())
    query = [(-1, -1)]
    mapping = {}
    edge_t = [[0, 0, 0, 0] for _ in range(m + 1)]
    edge = []
    arr = [[] for _ in range(4 * m + 1)]
    parent = [i for i in range(n + 1)]
    depth = [0 for _ in range(n + 1)]
    cnt = 0
    for i in range(1, m + 1):
        q, a, b = map(int, sys.stdin.readline().split())
        if a > b:
            a, b = b, a
        if q == 1:
            mapping[(a, b)] = i
            edge_t[i] = [a, b, cnt + 1, -1]
        elif q == 2:
            temp = mapping[(a, b)]
            edge_t[temp][3] = cnt
            edge.append(edge_t[temp])
        else:
            query.append((a, b))
            cnt += 1
    for i in range(1, m + 1):
        if edge_t[i][3] == -1:
            edge_t[i][3] = cnt
            edge.append(edge_t[i])
    for a, b, s, e in edge:
        update(arr, s, e, 1, cnt, 1, (a, b))
    stack = []
    solve(stack, query, depth, arr, parent, 1, cnt, 1)

    return

if __name__ == "__main__":
    main()