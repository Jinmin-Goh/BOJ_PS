# Problem No.: 15316
# Solver:      Jinmin Goh
# Date:        20220727
# URL: https://www.acmicpc.net/problem/15316

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
        print("YES" if res else "NO")
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
    edge_t = [[0, 0, 0, 0] for _ in range(400000 + 1)]
    edge = []
    arr = [[] for _ in range(4 * 200000 + 1)]
    parent = [i for i in range(200000 + 1)]
    depth = [0 for _ in range(200000 + 1)]
    cnt = 0
    input_edge = [(0, 0)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if a > b:
            a, b = b, a
        input_edge.append((a, b))
    on_set = set()
    status = list(map(int, sys.stdin.readline().split()))
    for i in range(1, m + 1):
        if status[i - 1] == 1:
            mapping[input_edge[i]] = i
            edge_t[i] = [input_edge[i][0], input_edge[i][1], cnt + 1, -1]
            on_set.add(input_edge[i])
    q = int(sys.stdin.readline().rstrip())
    for i in range(1, q + 1):
        temp = tuple(map(int, sys.stdin.readline().split()))
        if temp[0] == 1:
            _, a = temp
            if input_edge[a] in on_set:
                idx = mapping[input_edge[a]]
                edge_t[idx][3] = cnt
                edge.append(edge_t[idx])
                on_set.remove(input_edge[a])
            else:
                mapping[input_edge[a]] = i + m
                edge_t[i + m] = [input_edge[a][0], input_edge[a][1], cnt + 1, -1]
                on_set.add(input_edge[a])
        else:
            _, a, b = temp
            query.append((a, b))
            cnt += 1
    for i in range(1, 400000 + 1):
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