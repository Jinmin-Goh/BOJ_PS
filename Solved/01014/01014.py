# Problem No.: 1014
# Solver:      Jinmin Goh
# Date:        20220718
# URL: https://www.acmicpc.net/problem/1014

import sys

def dfs(adj, left, right, visited, curr):
    visited[curr] = True
    for i in range(len(adj[curr])):
        next = adj[curr][i]
        if right[next] == -1 or (not visited[right[next]] and dfs(adj, left, right, visited, right[next])):
            left[curr] = next
            right[next] = curr
            return True
    return False

def main():
    t = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        table = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
        adj = [[] for _ in range(m * n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if table[i][j] == '.':
                    ans += 1
        dir = [[-1, 0, 1, -1, 0, 1], [-1, -1, -1, 1, 1, 1]]
        for i in range(n):
            for j in range(m):
                for k in range(6):
                    if table[i][j] == 'x':
                        continue
                    i_next = i + dir[0][k]
                    j_next = j + dir[1][k]
                    if i_next >= 0 and i_next < n and j_next >= 0 and j_next < m and table[i_next][j_next] == '.':
                        adj[i * m + j].append(i_next * m + j_next)
        match = 0
        left = [-1 for _ in range(n * m)]
        right = [-1 for _ in range(n * m)]
        for i in range(n):
            for j in range(0, m, 2):
                visited = [False for _ in range(n * m)]
                if dfs(adj, left, right, visited, i * m + j):
                    match += 1
        print(ans - match)
    return

if __name__ == "__main__":
    main()