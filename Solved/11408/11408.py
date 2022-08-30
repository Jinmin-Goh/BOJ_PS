# Problem No.: 11408
# Solver:      Jinmin Goh
# Date:        20220830
# URL: https://www.acmicpc.net/problem/11408

import sys

def solve(graph, capacity, flow, cost, s, t):
    ret = 0
    cnt = 0
    while True:
        parent = [-1 for _ in range(810)]
        distance = [10 ** 9 for _ in range(810)]
        in_queue = [False for _ in range(810)]
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
        cnt += 1
    return (cnt, ret)

def main():
    graph = [[] for _ in range(810)]
    capacity = [[0 for _ in range(810)] for _ in range(810)]
    flow = [[0 for _ in range(810)] for _ in range(810)]
    cost = [[0 for _ in range(810)] for _ in range(810)]
    n, m = map(int, sys.stdin.readline().split())     
    for i in range(1, m + 1):
        graph[i + 400].append(801)
        graph[801].append(i + 400)
        capacity[i + 400][801] = 1
    for i in range(1, n + 1):
        graph[i].append(0)
        graph[0].append(i)
        capacity[0][i] = 1
        temp = list(map(int, sys.stdin.readline().split()))
        for j in range(temp[0]):
            a, c = temp[2 * j + 1], temp[2 * (j + 1)]
            graph[i].append(a + 400)
            graph[a + 400].append(i)
            cost[i][a + 400] = c
            cost[a + 400][i] = -c
            capacity[i][a + 400] = 1
    total_flow, total_cost = solve(graph, capacity, flow, cost, 0, 801)
    print(total_flow)
    print(total_cost)
    return

if __name__ == "__main__":
    main()