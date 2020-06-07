# Problem No.: 7576
# Solver:      Jinmin Goh
# Date:        20200607
# URL: https://www.acmicpc.net/problem/7576

import sys
import collections

def main():
    m, n = map(int, input().split())
    table = []
    for _ in range(n):
        table.append(list(map(int, sys.stdin.readline().split())))
    for i in range(n):
        for j in range(m):
            if table[i][j] == 1:
                nodeList = collections.deque([[i, j]])
                cnt = 0
                while nodeList:
                    cnt += 1
                    nodeList.append(None)
                    while True:
                        temp = nodeList.popleft()
                        #print(temp)
                        if temp == None:
                            break
                        x, y = temp[0], temp[1]
                        if table[x][y] == -1:
                            continue
                        elif table[x][y] == 0:
                            table[x][y] = cnt
                            if x > 0:
                                nodeList.append([x - 1, y])
                            if x < n - 1:
                                nodeList.append([x + 1, y])
                            if y > 0:
                                nodeList.append([x, y - 1])
                            if y < n - 1:
                                nodeList.append([x, y + 1])
                        else:
                            if table[x][y] == 1:
                                if x > 0:
                                    nodeList.append([x - 1, y])
                                if x < n - 1:
                                    nodeList.append([x + 1, y])
                                if y > 0:
                                    nodeList.append([x, y - 1])
                                if y < n - 1:
                                    nodeList.append([x, y + 1])
                            else:
                                table[x][y] = min(cnt, table[x][y])
    ans = 0
    #print(ans)
    #print(table)
    for i in range(n):
        for j in range(m):
            if table[i][j] == 0:
                print(-1)
                return
            #print(ans, table[i][j])
            ans = max(ans, table[i][j])
    print(ans - 1)
    return

if __name__ == "__main__":
    main()