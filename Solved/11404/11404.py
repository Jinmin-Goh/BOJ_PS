# Problem No.: 11404
# Solver:      Jinmin Goh
# Date:        20200604
# URL: https://www.acmicpc.net/problem/11404

import sys

def main():
    n = int(input())
    m = int(input())
    graph = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
    #node = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a][b] = min(graph[a][b], c)
        #node[a][b] = a
    for i in range(1, n + 1):
        graph[i][i] = 0
        for j in range(1, n + 1):
            if i == j:
                continue
            for k in range(1, n + 1):
                if i == k:
                    continue
                if graph[j][i] + graph[i][k] < graph[j][k]:
                    graph[j][k] = graph[j][i] + graph[i][k]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == sys.maxsize:
                print(0, end = "")
            else:
                print(graph[i][j], end = "")
            if j == n:
                continue
            print(" ", end = "")
        if i == n:
            break
        print("")
    return

if __name__ == "__main__":
    main()