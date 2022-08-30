# Problem No.: 2367
# Solver:      Jinmin Goh
# Date:        20220829
# URL: https://www.acmicpc.net/problem/2367

import sys

def solve(graph, capacity, flow, s, t):
    ans = 0
    while True:
        parent = [-1 for _ in range(310)]
        queue = [s]
        while queue and parent[t] == -1:
            temp = []
            for curr in queue:
                for next in graph[curr]:
                    if capacity[curr][next] - flow[curr][next] > 0 and parent[next] == -1:
                        temp.append(next)
                        parent[next] = curr
            queue = temp
        if parent[t] == -1:
            break
        val = 10 ** 6
        curr = t
        while curr != s:
            val = min(val, capacity[parent[curr]][curr] - flow[parent[curr]][curr])
            curr = parent[curr]
        curr = t
        while curr != s:
            flow[parent[curr]][curr] += val
            flow[curr][parent[curr]] -= val
            curr = parent[curr]
        ans += val
    return ans

def main():
    n, k, d = map(int, sys.stdin.readline().split())
    food = list(map(int, sys.stdin.readline().split()))
    graph = [[] for _ in range(310)]
    flow = [[0 for _ in range(310)] for _ in range(310)]
    capacity = [[0 for _ in range(310)] for _ in range(310)]
    for i in range(1, n + 1):
        graph[0].append(i)
        graph[i].append(0)
        capacity[0][i] = k
        temp = list(map(int, sys.stdin.readline().split()))
        for j in temp[1:]:
            graph[i].append(j + 200)
            graph[j + 200].append(i)
            capacity[i][j + 200] = 1
    for i in range(d):
        capacity[i + 201][301] = food[i]
        graph[i + 201].append(301)
    ans = solve(graph, capacity, flow, 0, 301)
    print(ans)

    return

if __name__ == "__main__":
    main()