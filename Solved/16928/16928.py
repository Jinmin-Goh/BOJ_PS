# Problem No.: 16928
# Solver:      Jinmin Goh
# Date:        20220613
# URL: https://www.acmicpc.net/problem/16928

import sys

def main():
    # parsing
    n, m = input().split()
    n, m = int(n), int(m)
    nDict = {}
    mDict = {}
    for _ in range(n):
        a, b = input().split()
        nDict[int(a) - 1] = int(b) - 1
    for _ in range(m):
        a, b = input().split()
        mDict[int(a) - 1] = int(b) - 1
    # graph construction
    graph = [[False for _ in range(100)] for _ in range(100)]
    for i in range(100):
        if i in nDict or i in mDict:
            continue
        for j in range(1, 7):
            if i + j >= 100:
                break
            elif i + j in nDict:
                graph[i][nDict[i + j]] = True
            elif i + j in mDict:
                graph[i][mDict[i + j]] = True
            else:
                graph[i][i + j] = True
    # BFS
    ans = 0
    current = [0]
    check = [False for _ in range(100)]
    ansFlag = False
    while True:
        temp = []
        for node in current:
            if node == 99:
                ansFlag = True
                break
            if check[node]:
                continue
            for i in range(100):
                if graph[node][i]:
                    temp.append(i)
            check[node] = True
        if ansFlag:
            break
        current = temp[:]
        ans += 1
    print(ans)
    return

if __name__ == "__main__":
    main()