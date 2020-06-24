# Problem No.: 16236
# Solver:      Jinmin Goh
# Date:        20200623
# URL: https://www.acmicpc.net/problem/16236

import sys
import collections

def main():
    n = int(input())
    table = []
    for _ in range(n):
        table.append(list(map(int, sys.stdin.readline().split())))
    
    sharkPos = None
    sharkLvl = [2, 0]
    

    oneFlag = False
    for i in range(n):
        for j in range(n):
            if table[i][j] == 9:
                sharkPos = [i, j]
                
                table[i][j] = 0
            if table[i][j] == 1:
                oneFlag = True
    
    if not oneFlag:
        print(0)
        return
    
    ans = 0

    while True:
        stack = collections.deque([])
        stack.append(sharkPos)
        dist = 0
        candPos = None
        tempVisited = [[False] * n for _ in range(n)]
        while stack:
            stack.append(None)
            while stack:
                temp = stack.popleft()
                if temp == None:
                    break
                x, y = temp[0], temp[1]
                if tempVisited[x][y]:
                    continue
                tempVisited[x][y] = True

                if table[x][y] > sharkLvl[0]:
                    continue
                
                if 0 < table[x][y] < sharkLvl[0]:
                    if not candPos:
                        candPos = [x, y]
                    else:
                        if candPos[0] > x:
                            candPos = [x, y]
                        elif candPos[0] == x and candPos[1] > y:
                            candPos = [x, y]
                    continue

                if x > 0 and not tempVisited[x - 1][y]:
                    stack.append([x - 1, y])
                if y > 0 and not tempVisited[x][y - 1]:
                    stack.append([x, y - 1])
                if y < n - 1 and not tempVisited[x][y + 1]:
                    stack.append([x, y + 1])
                if x < n - 1 and not tempVisited[x + 1][y]:
                    stack.append([x + 1, y])
                
            if candPos:
                #print("check")
                break
            dist += 1

        if candPos == None:
            break
        ans += dist
        table[candPos[0]][candPos[1]] = 0
        sharkPos = [candPos[0], candPos[1]]
        sharkLvl[1] += 1
        if sharkLvl[0] == sharkLvl[1]:
            sharkLvl[0] += 1
            sharkLvl[1] = 0
    
    print(ans)
        

    return

if __name__ == "__main__":
    main()