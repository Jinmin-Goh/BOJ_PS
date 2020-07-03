# Problem No.: 1916
# Solver:      Jinmin Goh
# Date:        20200701
# URL: https://www.acmicpc.net/problem/1916

import sys
import heapq
import collections

def main():
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n + 1)]
    distance = [sys.maxsize] * (n + 1)
    path = [None] * (n + 1)
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append([b, c])
        
    start, destination = map(int, input().split())
    distance[start] = 0
    path[start] = -1
    visited = [False] * (n + 1)

    minHeap = [[0, start]]
    while minHeap:
        temp = heapq.heappop(minHeap)
        if visited[temp[1]]:
            continue
        visited[temp[1]] = True
        dist = temp[0]
        currNode = temp[1]
        for adjNode in graph[currNode]:
            if distance[adjNode[0]] > dist + adjNode[1]:
                path[adjNode[0]] = currNode
                distance[adjNode[0]] = dist + adjNode[1]
                heapq.heappush(minHeap, [distance[adjNode[0]], adjNode[0]])
    print(distance[destination])

if __name__ == "__main__":
    main()