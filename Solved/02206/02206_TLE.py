# Problem No.: 2206
# Solver:      Jinmin Goh
# Date:        20200604
# URL: https://www.acmicpc.net/problem/2206

import sys

def main():
    n, m = map(int, input().split())
    table = []
    for _ in range(n):
        temp = sys.stdin.readline().strip()
        table.append([i for i in temp])
    stack = [(0, 0)]
    visited = set()
    nearSet = set()
    ansFlag = False
    cnt = 0
    while stack:
        cnt += 1
        stack.append((-1, -1))
        while stack:
            i = stack.pop(0)
            if i == (n - 1, m - 1):
                ansFlag = True
                break
            if i == (-1, -1):
                break
            if i in visited:
                continue
            visited.add(i)
            if i[0] > 0:
                if table[i[0] - 1][i[1]] == "0":
                    stack.append((i[0] - 1, i[1]))
                else:
                    nearSet.add((i[0] - 1, i[1]))
            if i[0] < n - 1:
                if table[i[0] + 1][i[1]] == "0":
                    stack.append((i[0] + 1, i[1]))
                else:
                    nearSet.add((i[0] + 1, i[1]))
            if i[1] > 0:
                if table[i[0]][i[1] - 1] == "0":
                    stack.append((i[0], i[1] - 1))
                else:
                    nearSet.add((i[0], i[1] - 1))
            if i[1] < m - 1:
                if table[i[0]][i[1] + 1] == "0":
                    stack.append((i[0], i[1] + 1))
                else:
                    nearSet.add((i[0], i[1] + 1))
        if ansFlag:
            break
    if ansFlag:
        print(cnt)
        return
    nearList = list(nearSet)
    #print(nearList)
    for a in nearList:
        table[a[0]][a[1]] = "0"
        #print(table)
        stack = [(0, 0)]
        visited = set()
        cnt = 0
        #print(table)
        while stack:
            cnt += 1
            stack.append((-1, -1))
            while stack:
                i = stack.pop(0)
                if i == (n - 1, m - 1):
                    ansFlag = True
                    break
                if i == (-1, -1):
                    break
                if i in visited:
                    continue
                visited.add(i)
                if i[0] > 0:
                    if table[i[0] - 1][i[1]] == "0":
                        stack.append((i[0] - 1, i[1]))
                if i[0] < n - 1:
                    if table[i[0] + 1][i[1]] == "0":
                        stack.append((i[0] + 1, i[1]))
                if i[1] > 0:
                    if table[i[0]][i[1] - 1] == "0":
                        stack.append((i[0], i[1] - 1))
                if i[1] < m - 1:
                    if table[i[0]][i[1] + 1] == "0":
                        stack.append((i[0], i[1] + 1))
            if ansFlag:
                break
        if ansFlag:
            print(cnt)
            return
        table[a[0]][a[1]] = "1"
    print(-1)
    return

if __name__ == "__main__":
    main()