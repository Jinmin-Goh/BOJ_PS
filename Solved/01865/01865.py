# Problem No.: 1865
# Solver:      Jinmin Goh
# Date:        20200603
# URL: https://www.acmicpc.net/problem/1865

import sys

def main():
    t = int(input())
    for _ in range(t):
        n, m, w = map(int, sys.stdin.readline().split())
        # graph parsing
        graph = [{} for __ in range(n + 1)]
        for __ in range(m):
            a, b, c = map(int, sys.stdin.readline().split())
            if b not in graph[a]:
                graph[a][b] = c
            else:
                graph[a][b] = min(graph[a][b], c)
            if a not in graph[b]:
                graph[b][a] = c
            else:
                graph[b][a] = min(graph[b][a], c)
        for __ in range(w):
            a, b, c = map(int, sys.stdin.readline().split())
            if b not in graph[a]:
                graph[a][b] = -c
            else:
                graph[a][b] = min(graph[a][b], -c)
        # Bellman-Ford's algorithm
        # start from node 1
        distance = [sys.maxsize] * (n + 1)
        distance[1] = 0
        #print(graph)
        for __ in range(n - 1):
            for i in range(1, n + 1):
                for j in graph[i]:
                    if distance[j] > distance[i] + graph[i][j]:
                        distance[j] = distance[i] + graph[i][j]
        #print(distance)
        temp = distance[:]
        for i in range(1, n + 1):
            for j in graph[i]:
                if distance[j] > distance[i] + graph[i][j]:
                    distance[j] = distance[i] + graph[i][j]
        #print(distance)
        if temp != distance:
            print("YES")
        else:
            print("NO")
    return

if __name__ == "__main__":
    main()