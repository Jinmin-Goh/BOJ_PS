# Problem No.: 13141
# Solver:      Jinmin Goh
# Date:        20220802
# URL: https://www.acmicpc.net/problem/13141

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[[0, 0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
    loop = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                graph[i][j][0] = 10000000
    for _ in range(m):
        a, b, w = map(int, sys.stdin.readline().split())
        if a == b:
            loop[a] = max(loop[a], w)
        else:
            graph[a][b][0] = min(w, graph[a][b][0])
            graph[a][b][1] = max(w, graph[a][b][1])
            graph[a][b][2] = min(w, graph[a][b][2])
            graph[b][a][0] = min(w, graph[b][a][0])
            graph[b][a][1] = max(w, graph[b][a][1])
            graph[b][a][2] = min(w, graph[b][a][2])
    # Floyd-Warshall
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j][0] = min(graph[i][j][0], graph[i][k][0] + graph[k][j][0])
    ans = 10000000.0
    for node in range(1, n + 1):
        temp = 0.0
        for i in range(1, n + 1):
            # self loop
            if loop[i] != 0:
                temp = max(temp, graph[node][i][0] + loop[i] / 2)
            # burn time calculate
            for j in range(1, n + 1):
                if graph[i][j][1] > 0 and graph[i][j][1] != graph[i][j][2]:
                    longer = max(graph[node][i][0], graph[node][j][0])
                    t = (graph[i][j][1] - abs(graph[node][i][0] - graph[node][j][0])) / 2
                    temp = max(temp, longer + t)
        ans = min(ans, temp)
    print(ans)

    
    return

if __name__ == "__main__":
    main()
