# Problem No.: 1753
# Solver:      Jinmin Goh
# Date:        20200602
# URL: https://www.acmicpc.net/problem/1753

import sys
import heapq

# Dijkstra's algorithm
def main():
    n, m = map(int, input().split())
    startNode = int(input())
    graph = [{} for _ in range(n + 1)]
    
    # initialization
    ans = [sys.maxsize] * (n + 1)   # 100 is same to INF; all weight is same or smaller than 10
    ans[startNode] = 0
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        if b in graph[a]:
            graph[a][b] = min(c, graph[a][b])
        else:
            graph[a][b] = c

    queue = [[0, startNode]]
    #print(ans)
    while queue:
        # minimum distance
        temp = heapq.heappop(queue)
        currDist = temp[0]
        currNode = temp[1]
        
        # adjacent node search
        for i in list(graph[currNode].keys()):
            temp = graph[currNode][i] + currDist
            #print(temp)
            if temp < ans[i]:
                ans[i] = temp
                heapq.heappush(queue, [temp, i])
        #print(ans)
    for i in range(1, n + 1):
        if ans[i] == sys.maxsize:
            print("INF")
        else:
            print(ans[i])
    return

if __name__ == "__main__":
    main()