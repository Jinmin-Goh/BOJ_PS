# Problem No.: 1520
# Solver:      Jinmin Goh
# Date:        20200319
# URL: https://www.acmicpc.net/problem/1520

import sys

sys.setrecursionlimit(1000000)

def DFS(mapHeight: [[int]], i: int, j: int, dpTable: [[int]]) -> bool:
    if i == len(mapHeight) - 1 and j == len(mapHeight[0]) - 1:
        return True
    if dpTable[i][j] != -1:
        if dpTable[i][j] == 0:
            return False
        else:
            return True
    dpTable[i][j] = 0
    temp = mapHeight[i][j]
    mapHeight[i][j] = -1
    if i < len(mapHeight) - 1 and temp > mapHeight[i + 1][j] and mapHeight[i + 1][j] != -1:
        if DFS(mapHeight, i + 1, j, dpTable):
            dpTable[i][j] += dpTable[i + 1][j]
    if i > 0 and temp > mapHeight[i - 1][j] and mapHeight[i - 1][j] != -1:
        if DFS(mapHeight, i - 1, j, dpTable):
            dpTable[i][j] += dpTable[i - 1][j]
    if j < len(mapHeight[0]) - 1 and temp > mapHeight[i][j + 1] and mapHeight[i][j + 1] != -1:
        if DFS(mapHeight, i, j + 1, dpTable):
            dpTable[i][j] += dpTable[i][j + 1]
    if j > 0 and temp > mapHeight[i][j - 1] and mapHeight[i][j - 1] != -1:
        if DFS(mapHeight, i, j - 1, dpTable):
            dpTable[i][j] += dpTable[i][j - 1]
    mapHeight[i][j] = temp
    if dpTable[i][j]:
        return True
    else:
        return False

def main():
    nrow, ncol = map(int, input().split())
    mapHeight = []
    for i in range(nrow):
        mapHeight.append(list(map(int, sys.stdin.readline().split())))
    dpTable = [[-1] * ncol for i in range(nrow)]
    dpTable[-1][-1] = 1
    DFS(mapHeight, 0, 0, dpTable)
    #print(dpTable)
    print(dpTable[0][0])
    return

if __name__ == "__main__":
    main()