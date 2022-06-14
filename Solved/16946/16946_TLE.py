# Problem No.: 16946
# Solver:      Jinmin Goh
# Date:        20220614
# URL: https://www.acmicpc.net/problem/16946

import sys

# TLE; O(n^2 m^2) naive solution
def main():
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    ans = [[0 for _ in range(m)] for __ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "1":
                search = [(i, j)]
                cnt = 1
                visited = [[False for _ in range(m)] for __ in range(n)]
                while search:
                    temp = []
                    for node in search:
                        if visited[node[0]][node[1]]:
                            continue
                        if arr[node[0]][node[1]] == "0":
                            cnt += 1
                        visited[node[0]][node[1]] = True
                        if node[0] > 0 and arr[node[0] - 1][node[1]] == "0":
                            temp.append((node[0] - 1, node[1]))
                        if node[0] < n - 1 and arr[node[0] + 1][node[1]] == "0":
                            temp.append((node[0] + 1, node[1]))
                        if node[1] > 0 and arr[node[0]][node[1] - 1] == "0":
                            temp.append((node[0], node[1] - 1))
                        if node[1] < m - 1 and arr[node[0]][node[1] + 1] == "0":
                            temp.append((node[0], node[1] + 1))
                    search = temp
                ans[i][j] = cnt % 10
    for i in range(n):
        for j in range(m):
            print(ans[i][j], end="")
        print()
    return

if __name__ == "__main__":
    main()