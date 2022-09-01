# Problem No.: 2316
# Solver:      Jinmin Goh
# Date:        20220901
# URL: https://www.acmicpc.net/problem/2316

import sys

def solve(graph, capacity, flow, s, t):
    ans = 0
    while True:
        parent = [-1 for _ in range(810)]
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
        val = 10 ** 10
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
    n, p = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(810)]
    capacity = [[0 for _ in range(810)] for _ in range(810)]
    flow = [[0 for _ in range(810)] for _ in range(810)]
    for i in range(1, n + 1):
        graph[i].append(i + 400)
        graph[i + 400].append(i)
        capacity[i][i + 400] = 1
    for _ in range(p):
        a, b = map(int, sys.stdin.readline().split())
        graph[a + 400].append(b)
        graph[b].append(a + 400)
        graph[a].append(b + 400)
        graph[b + 400].append(a)
        capacity[a + 400][b] = 1
        capacity[b + 400][a] = 1
    ans = solve(graph, capacity, flow, 401, 2)
    print(ans)
    return

if __name__ == "__main__":
    main()