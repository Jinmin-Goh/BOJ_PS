# Problem No.: 3640
# Solver:      Jinmin Goh
# Date:        20220831
# URL: https://www.acmicpc.net/problem/3640

import sys

def solve(graph, capacity, flow, cost, s, t):
    ret = 0
    while True:
        parent = [-1 for _ in range(2010)]
        distance = [10 ** 9 for _ in range(2010)]
        in_queue = [False for _ in range(2010)]
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
    return ret

def main():
    temp = sys.stdin.readline().rstrip()
    while temp:
        n, m = map(int, temp.split())
        graph = [[] for _ in range(2010)]
        capacity = [[0 for _ in range(2010)] for _ in range(2010)]
        flow = [[0 for _ in range(2010)] for _ in range(2010)]
        cost = [[0 for _ in range(2010)] for _ in range(2010)]
        for i in range(1, n + 1):
            graph[i].append(i + 1000)
            graph[i + 1000].append(i)
            if i == 1 or i == n:
                capacity[i][i + 1000] = 2
            else:
                capacity[i][i + 1000] = 1
        for _ in range(m):
            a, b, c = map(int, sys.stdin.readline().split())
            graph[a + 1000].append(b)
            graph[b].append(a + 1000) 
            capacity[a + 1000][b] = 1
            cost[a + 1000][b] = c
            if cost[b][a + 1000] == 0:
                cost[b][a + 1000] = -c
        graph[0].append(1)
        graph[1].append(0)
        capacity[0][1] = 2
        graph[n + 1000].append(2001)
        graph[2001].append(n + 1000)
        capacity[n + 1000][2001] = 2
        
        ans = solve(graph, capacity, flow, cost, 1, 2001)
        print(ans)
        del graph, capacity, flow, cost
        temp = sys.stdin.readline().rstrip()

    return

if __name__ == "__main__":
    main()