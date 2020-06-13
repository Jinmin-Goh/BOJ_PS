# Problem No.: 11403
# Solver:      Jinmin Goh
# Date:        20200612
# URL: https://www.acmicpc.net/problem/11403

import sys

def main():
    n = int(input())
    graph = [[] for _ in range(n)]
    for i in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        for j in range(n):
            if temp[j]:
                graph[i].append(j)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        stack = [i]
        visited = [False] * n
        visited[i] = 0
        while stack:
            temp = stack.pop()
            if temp == i:
                if visited[i] > 1:
                    continue
                elif visited[i] == 1:
                    ans[i][i] = 1
                visited[i] += 1
            elif visited[temp]:
                continue
            else:
                visited[temp] = True
                ans[i][temp] = 1
            stack += graph[temp]
    for i in range(n):
        for j in range(n):
            print(ans[i][j], end = " ")
        print("")
            

    return

if __name__ == "__main__":
    main()