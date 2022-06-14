# Problem No.: 16946
# Solver:      Jinmin Goh
# Date:        20220614
# URL: https://www.acmicpc.net/problem/16946

import sys

def main():
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    ans = [[0 for _ in range(m)] for __ in range(n)]
    cntArr = [[0 for _ in range(m)] for __ in range(n)]
    tag = 1
    visited = [[False for _ in range(m)] for __ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "0" and cntArr[i][j] == 0:
                search = [(i, j)]
                cnt = 0
                visitedCoor = []
                while search:
                    temp = []
                    for node in search:
                        if visited[node[0]][node[1]]:
                            continue
                        if arr[node[0]][node[1]] == "0":
                            cnt += 1
                        visited[node[0]][node[1]] = True
                        visitedCoor.append(node)
                        if node[0] > 0 and arr[node[0] - 1][node[1]] == "0":
                            temp.append((node[0] - 1, node[1]))
                        if node[0] < n - 1 and arr[node[0] + 1][node[1]] == "0":
                            temp.append((node[0] + 1, node[1]))
                        if node[1] > 0 and arr[node[0]][node[1] - 1] == "0":
                            temp.append((node[0], node[1] - 1))
                        if node[1] < m - 1 and arr[node[0]][node[1] + 1] == "0":
                            temp.append((node[0], node[1] + 1))
                    search = temp
                for node in visitedCoor:
                    cntArr[node[0]][node[1]] = (cnt % 10, tag)
                tag += 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "1":
                ans[i][j] += 1
                tagSet = set()
                if i > 0 and arr[i - 1][j] == "0" and cntArr[i - 1][j][1] not in tagSet:
                    ans[i][j] += cntArr[i - 1][j][0]
                    tagSet.add(cntArr[i - 1][j][1])
                if i < n - 1 and arr[i + 1][j] == "0" and cntArr[i + 1][j][1] not in tagSet:
                    ans[i][j] += cntArr[i + 1][j][0]
                    tagSet.add(cntArr[i + 1][j][1])
                if j > 0 and arr[i][j - 1] == "0" and cntArr[i][j - 1][1] not in tagSet:
                    ans[i][j] += cntArr[i][j - 1][0]
                    tagSet.add(cntArr[i][j - 1][1])
                if j < m - 1 and arr[i][j + 1] == "0" and cntArr[i][j + 1][1] not in tagSet:
                    ans[i][j] += cntArr[i][j + 1][0]
                    tagSet.add(cntArr[i][j + 1][1])
                ans[i][j] %= 10
                
    for i in range(n):
        for j in range(m):
            print(ans[i][j], end="")
        print()
    return

if __name__ == "__main__":
    main()