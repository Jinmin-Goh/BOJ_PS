# Problem No.: 2359
# Solver:      Jinmin Goh
# Date:        20220818
# URL: https://www.acmicpc.net/problem/2359

import sys

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x == y:
        return
    if x < y:
        parent[x] = y
    else:
        parent[y] = x
    return

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def main():
    n, m, s, t = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    weight_list = []
    for _ in range(m):
        a, b, w = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
        weight_list.append((w, a, b))
    weight_list.sort()
    ans = 10 ** 15
    ans_set = set()
    for i in range(len(weight_list)):
        parent = [k for k in range(n + 1)]
        temp = {weight_list[i][1], weight_list[i][2]}
        union(parent, weight_list[i][1], weight_list[i][2])
        max_val = weight_list[i][0]
        min_val = weight_list[i][0]
        for j in range(i, len(weight_list)):
            union(parent, weight_list[j][1], weight_list[j][2])
            max_val = max(max_val, weight_list[j][0])
            min_val = min(min_val, weight_list[j][0])
            temp.add((min(weight_list[j][1], weight_list[j][2]), max(weight_list[j][1], weight_list[j][2])))
            if find(parent, s) == find(parent, t):
                if ans > (max_val - min_val):
                    ans = max_val - min_val
                    ans_set = temp
                    break
    print(ans)
    queue = [[s, [s]]]
    visited = [False for _ in range(n + 1)]
    ans_list = []
    while queue:
        temp = []
        for node, path in queue:
            if node == t:
                ans_list = path
                break
            if visited[node]:
                continue
            visited[node] = True
            for next in graph[node]:
                if (min(node, next), max(node, next)) not in ans_set:
                    continue
                temp_path = path[:]
                temp_path.append(next)
                temp.append([next, temp_path])
        queue = temp
    for i in ans_list:
        print(i, end=' ')
    return

if __name__ == "__main__":
    main()