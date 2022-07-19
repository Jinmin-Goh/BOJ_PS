# Problem No.: 5719
# Solver:      Jinmin Goh
# Date:        20220719
# URL: https://www.acmicpc.net/problem/5719

import sys, heapq

def main():
    n, m = map(int, sys.stdin.readline().split())
    while n != 0 and m != 0:
        s, d = map(int, sys.stdin.readline().split())
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v, w = map(int, sys.stdin.readline().split())
            graph[u].append((v, w))
        # 1st dijkstra
        parent = [[] for _ in range(n)]
        pq = [(s, 0)]
        dist = [10 ** 8 for _ in range(n)]
        dist[s] = 0
        while pq:
            curr, curr_w = heapq.heappop(pq)
            if curr_w > dist[curr]:
                continue
            for next, next_w in graph[curr]:
                if dist[next] > dist[curr] + next_w:
                    dist[next] = dist[curr] + next_w
                    parent[next] = [curr]
                    heapq.heappush(pq, (next, dist[next]))
                elif dist[next] == dist[curr] + next_w:
                    parent[next].append(curr)
        # path remove
        stack = [d]
        visited = [False for _ in range(n)]
        while stack:
            temp = []
            for node in stack:
                if visited[node]:
                    continue
                visited[node] = True
                for p in parent[node]:
                    for i in range(len(graph[p])):
                        if graph[p][i][0] == node:
                            graph[p][i] = (-1, -1)
                    temp.append(p)
            stack = temp
        # 2nd dijkstra
        parent = [[] for _ in range(n)]
        pq = [(s, 0)]
        dist = [10 ** 8 for _ in range(n)]
        dist[s] = 0
        while pq:
            curr, curr_w = heapq.heappop(pq)
            if curr_w > dist[curr]:
                continue
            for next, next_w in graph[curr]:
                if next == -1:
                    continue
                if dist[next] > dist[curr] + next_w:
                    dist[next] = dist[curr] + next_w
                    parent[next] = [curr]
                    heapq.heappush(pq, (next, dist[next]))
                elif dist[next] == dist[curr] + next_w:
                    parent[next].append(curr)
        print(dist[d] if dist[d] != 10 ** 8 else -1)
        n, m = map(int, sys.stdin.readline().split())
    return

if __name__ == "__main__":
    main()