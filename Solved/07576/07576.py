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
    startList = collections.deque([])
    for i in range(n):
        for j in range(m):
            if table[i][j] == 1:
                startList.append((i, j))
    if not startList:
        print(-1)
        return
    cnt = 0
    visited = set()
    while startList:
        cnt += 1
        startList.append(None)
        #print(startList)
        while True:
            temp = startList.popleft()
            #print(temp)
            if temp == None:
                break
            if temp in visited:
                continue
            visited.add(temp)
            x, y = temp[0], temp[1]
            if table[x][y] == 0:
                table[x][y] = cnt
                if x > 0 and table[x - 1][y] == 0:
                    startList.append((x - 1, y))
                if x < n - 1 and table[x + 1][y] == 0:
                    startList.append((x + 1, y))
                if y > 0 and table[x][y - 1] == 0:
                    startList.append((x, y - 1))
                if y < m - 1 and table[x][y + 1] == 0:
                    startList.append((x, y + 1))
            elif table[x][y] == 1:
                if x > 0 and table[x - 1][y] == 0:
                    startList.append((x - 1, y))
                if x < n - 1 and table[x + 1][y] == 0:
                    startList.append((x + 1, y))
                if y > 0 and table[x][y - 1] == 0:
                    startList.append((x, y - 1))
                if y < m - 1 and table[x][y + 1] == 0:
                    startList.append((x, y + 1))
            else:
                continue
        #print(startList)
                
    ans = 0
    #print(table)
    for i in range(n):
        for j in range(m):
            if table[i][j] == 0:
                print(-1)
                return
            ans = max(ans, table[i][j])
    print(ans - 1)
    return

if __name__ == "__main__":
    main()