# Problem No.: 7569
# Solver:      Jinmin Goh
# Date:        20200607
# URL: https://www.acmicpc.net/problem/7569

import sys
import collections

def main():
    m, n, h = map(int, input().split())
    table = []
    for __ in range(h):
        table.append([])
        for _ in range(n):
            table[-1].append(list(map(int, sys.stdin.readline().split())))
    
    startList = collections.deque([])
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if table[i][j][k] == 1:
                    startList.append((i, j, k))
    #print(startList)
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
            x, y, z = temp[0], temp[1], temp[2]
            #print(x, y, z, table[x][y][z])
            if table[x][y][z] == 0:
                table[x][y][z] = cnt
                if x > 0 and table[x - 1][y][z] == 0:
                    startList.append((x - 1, y, z))
                if x < h - 1 and table[x + 1][y][z] == 0:
                    startList.append((x + 1, y, z))
                if y > 0 and table[x][y - 1][z] == 0:
                    startList.append((x, y - 1, z))
                if y < n - 1 and table[x][y + 1][z] == 0:
                    startList.append((x, y + 1, z))
                if z > 0 and table[x][y][z - 1] == 0:
                    startList.append((x, y, z - 1))
                if z < m - 1 and table[x][y][z + 1] == 0:
                    startList.append((x, y, z + 1))
            elif table[x][y][z] == 1:
                if x > 0 and table[x - 1][y][z] == 0:
                    startList.append((x - 1, y, z))
                if x < h - 1 and table[x + 1][y][z] == 0:
                    startList.append((x + 1, y, z))
                if y > 0 and table[x][y - 1][z] == 0:
                    startList.append((x, y - 1, z))
                if y < n - 1 and table[x][y + 1][z] == 0:
                    startList.append((x, y + 1, z))
                if z > 0 and table[x][y][z - 1] == 0:
                    startList.append((x, y, z - 1))
                if z < m - 1 and table[x][y][z + 1] == 0:
                    startList.append((x, y, z + 1))
            else:
                continue
        #print(startList)
                
    ans = 0
    #print(table)
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if table[i][j][k] == 0:
                    print(-1)
                    return
                ans = max(ans, table[i][j][k])
    print(ans - 1)
    return

if __name__ == "__main__":
    main()