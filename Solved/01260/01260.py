# Problem No.: 1260
# Solver:      Jinmin Goh
# Date:        20200609
# URL: https://www.acmicpc.net/problem/1260

import sys
import collections

def main():
    n, m, startNode = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if a == b:
            return
        graph[a].append(b)
        graph[b].append(a)
    
    if n == 1:
        print(startNode)
        print(startNode)
        return

    bfsAns = []
    dfsAns = []

    #for i in graph:
    #    i = list(set(i))
        #i.sort()

    # BFS
    visited = [False] * (n + 1)
    stack = collections.deque([startNode])
    while stack:
        stack.append(None)
        while True:
            temp = stack.popleft()
            if temp == None:
                break
            if visited[temp]:
                continue
            visited[temp] = True
            bfsAns.append(temp)
            graph[temp].sort()
            stack += graph[temp]
    
    # DFS
    visited = [False] * (n + 1)
    stack = collections.deque([startNode])
    while stack:
        temp = stack.pop()
        if visited[temp]:
            continue
        visited[temp] = True
        dfsAns.append(temp)
        graph[temp].sort()
        stack += reversed(graph[temp])
        
    for i in dfsAns:
        print(i, end = " ")
    print("")
    for i in bfsAns:
        print(i, end = " ")
    return

if __name__ == "__main__":
    main()