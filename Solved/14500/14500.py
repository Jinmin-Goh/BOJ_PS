# Problem No.: 14500
# Solver:      Jinmin Goh
# Date:        20200618
# URL: https://www.acmicpc.net/problem/14500

import sys

def main():
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))
    
    ans = 0

    # 1-4 frame
    for i in range(n):
        for j in range(m - 3):
            sumVal = sum(graph[i][j:j + 4])
            ans = max(sumVal, ans)

    # 4-1 frame
    for i in range(n - 3):
        for j in range(m):
            sumVal = 0
            for p in range(4):
                sumVal += graph[i + p][j]
            ans = max(sumVal, ans)

    # 2-2 frame
    for i in range(n - 1):
        for j in range(m - 1):
            sumVal = 0
            for p in range(2):
                for q in range(2):
                    sumVal += graph[i + p][j + q]
            ans = max(sumVal, ans)

    # 2-3 frame
    for i in range(n - 1):
        for j in range(m - 2):
            temp = 0
            for p in range(2):
                for q in range(3):
                    temp += graph[i + p][j + q]
            
            sumVal = []
            # S
            sumVal.append(temp - (graph[i][j] + graph[i + 1][j + 2]))
            sumVal.append(temp - (graph[i + 1][j] + graph[i][j + 2]))
            # L
            sumVal.append(temp - (graph[i][j] + graph[i][j + 1]))
            sumVal.append(temp - (graph[i][j + 1] + graph[i][j + 2]))
            sumVal.append(temp - (graph[i + 1][j] + graph[i + 1][j + 1]))
            sumVal.append(temp - (graph[i + 1][j + 1] + graph[i + 1][j + 2]))
            # T
            sumVal.append(temp - (graph[i][j] + graph[i][j + 2]))
            sumVal.append(temp - (graph[i + 1][j] + graph[i + 1][j + 2]))

            ans = max(max(sumVal), ans)

    # 3-2 frame
    for i in range(n - 2):
        for j in range(m - 1):
            temp = 0
            for p in range(3):
                for q in range(2):
                    temp += graph[i + p][j + q]
            
            sumVal = []
            # S
            sumVal.append(temp - (graph[i][j] + graph[i + 2][j + 1]))
            sumVal.append(temp - (graph[i + 2][j] + graph[i][j + 1]))
            # L
            sumVal.append(temp - (graph[i][j] + graph[i + 1][j]))
            sumVal.append(temp - (graph[i + 1][j] + graph[i + 2][j]))
            sumVal.append(temp - (graph[i][j + 1] + graph[i + 1][j + 1]))
            sumVal.append(temp - (graph[i + 1][j + 1] + graph[i + 2][j + 1]))
            # T
            sumVal.append(temp - (graph[i][j] + graph[i + 2][j]))
            sumVal.append(temp - (graph[i][j + 1] + graph[i + 2][j + 1]))

            ans = max(max(sumVal), ans)
    
    print(ans)
    return

if __name__ == "__main__":
    main()