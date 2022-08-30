# Problem No.: 11407
# Solver:      Jinmin Goh
# Date:        20220830
# URL: https://www.acmicpc.net/problem/11407

import sys

def solve(graph, capacity, flow, cost, s, t):
    ret = 0
    cnt = 0
    while True:
        parent = [-1 for _ in range(210)]
        distance = [10 ** 9 for _ in range(210)]
        in_queue = [False for _ in range(210)]
        queue = [s]
        distance[s] = 0
        in_queue[s] = True
        while queue:
            temp = []
            for curr in queue:
                in_queue[curr] = False
                for next in graph[curr]:
                    if capacity[curr][next] - flow[curr][next] > 0 and distance[next] > distance[curr] + cost[curr][next]:
                        distance[next] = distance[curr] + cost[curr][next]
                        parent[next] = curr
                        if in_queue[next] == False:
                            in_queue[next] = True
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
            ret += val * cost[parent[curr]][curr]
            flow[parent[curr]][curr] += val
            flow[curr][parent[curr]] -= val
            curr = parent[curr]
        cnt += val
    return (cnt, ret)

def main():
    n, m = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    capacity = [[0 for _ in range(210)] for _ in range(210)]
    flow = [[0 for _ in range(210)] for _ in range(210)]
    cost = [[0 for _ in range(210)] for _ in range(210)]
    graph = [[] for _ in range(210)]
    for i in range(1, m + 1):
        temp = list(map(int, sys.stdin.readline().split()))
        for j in range(1, n + 1):
            capacity[j][i + 100] = temp[j - 1]
            graph[i + 100].append(j)
            graph[j].append(i + 100)
    for i in range(1, m + 1):
        temp = list(map(int, sys.stdin.readline().split()))
        for j in range(1, n + 1):
            cost[i + 100][j] = -temp[j - 1]
            cost[j][i + 100] = temp[j - 1]
    for i in range(n):
        graph[i + 1].append(0)
        graph[0].append(i + 1)
        capacity[0][i + 1] = A[i]
    for i in range(m):
        graph[i + 101].append(201)
        graph[201].append(i + 101)
        capacity[i + 101][201] = B[i]
    ans = solve(graph, capacity, flow, cost, 0, 201)
    print(ans[0])
    print(ans[1])
    return

if __name__ == "__main__":
    main()

