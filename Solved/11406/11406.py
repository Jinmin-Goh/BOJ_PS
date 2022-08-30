# Problem No.: 11406
# Solver:      Jinmin Goh
# Date:        20220830
# URL: https://www.acmicpc.net/problem/11406

import sys

def solve(graph, capacity, flow, s, t):
    ret = 0
    while True:
        parent = [-1 for _ in range(210)]
        queue = [s]
        while queue and parent[t] == -1:
            temp = []
            for curr in queue:
                for next in graph[curr]:
                    if capacity[curr][next] - flow[curr][next] > 0 and parent[next] == -1:
                        parent[next] = curr
                        temp.append(next)
            queue = temp
        if parent[t] == -1:
            break
        val = 10 ** 9
        curr = t
        while curr != s:
            val = min(val, capacity[parent[curr]][curr] - flow[parent[curr]][curr])
            curr = parent[curr]
        curr = t
        while curr != s:
            flow[parent[curr]][curr] += val
            flow[curr][parent[curr]] -= val
            curr = parent[curr]
        ret += val
    return ret

def main():
    n, m = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    capacity = [[0 for _ in range(210)] for _ in range(210)]
    flow = [[0 for _ in range(210)] for _ in range(210)]
    graph = [[] for _ in range(210)]
    for i in range(1, m + 1):
        temp = list(map(int, sys.stdin.readline().split()))
        for j in range(1, n + 1):
            graph[i + 100].append(j)
            graph[j].append(i + 100)
            capacity[j][i + 100] = temp[j - 1]
    for i in range(n):
        graph[i + 1].append(0)
        graph[0].append(i + 1)
        capacity[0][i + 1] = A[i]
    for i in range(m):
        graph[i + 101].append(201)
        graph[201].append(i + 101)
        capacity[i + 101][201] = B[i]
    ans = solve(graph, capacity, flow, 0, 201)
    print(ans)
    return

if __name__ == "__main__":
    main()

