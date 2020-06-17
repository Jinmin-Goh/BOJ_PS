# Problem No.: 9205
# Solver:      Jinmin Goh
# Date:        20200617
# URL: https://www.acmicpc.net/problem/9205

import sys

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        # graph[0]: start; graph[1]: end
        graph = [[] for __ in range(n + 2)]
        distance = []
        for i in range(n + 2):
            x, y = map(int, sys.stdin.readline().split())
            distance.append([x, y])
            for j in range(i):
                if abs(distance[j][0] - x) + abs(distance[j][1] - y) <= 1000:
                    graph[i].append(j)
                    graph[j].append(i)
        #print(graph)
        start = 0
        end = n + 1
        visited = [False] * (n + 2)
        stack = [start]
        flag = False
        while stack:
            temp = stack.pop()
            #print(temp, stack, visited)
            if temp == end:
                flag = True
                break
            if visited[temp]:
                continue
            visited[temp] = True
            stack += graph[temp]
        if flag:
            print("happy")
        else:
            print("sad")
                
                

    return

if __name__ == "__main__":
    main()