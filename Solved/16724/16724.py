# Problem No.: 16724
# Solver:      Jinmin Goh
# Date:        20220630
# URL: https://www.acmicpc.net/problem/16724

import sys

def main():
    n, m = map(int, input().split())
    table = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
    graph = [-1 for _ in range(n * m)]
    for i in range(n):
        for j in range(m):
            if table[i][j] == 'U':
                graph[i * m + j] = (i - 1) * m + j
            elif table[i][j] == 'D':
                graph[i * m + j] = (i + 1) * m + j
            elif table[i][j] == 'L':
                graph[i * m + j] = i * m + j - 1
            elif table[i][j] == 'R':
                graph[i * m + j] = i * m + j + 1
    visited = [0 for _ in range(n * m)]
    ans = 0
    for i in range(n * m):
        if visited[i] == 2:
            continue
        stack = [i]
        visited[i] = 1
        curr = i
        while visited[graph[curr]] == 0:
            curr = graph[curr]
            stack.append(curr)
            visited[curr] = 1
        if visited[graph[curr]] == 1:
            ans += 1
        while stack:
            visited[stack.pop()] = 2
    print(ans)
    return

if __name__ == "__main__":
    main()