# Problem No.: 1028
# Solver:      Jinmin Goh
# Date:        20200326
# URL: https://www.acmicpc.net/problem/1028

import sys

def main():
    R, C = map(int, input().split())
    mapTable = []
    sumVal = 0
    for _ in range(R):
        temp = input()
        tempList = []
        for i in temp:
            tempList.append(int(i))
        mapTable.append(tempList)
        sumVal += sum(mapTable[-1])
    if sumVal == 0:
        print(0)
        return
    maxSize = (min(R, C) + 1) // 2
    ans = 1
    # memorize max length of coutinuous 1s on each direction; L: left, R: right, D: down, U: up
    LDTable = [[0] * C for _ in range(R)]
    RDTable = [[0] * C for _ in range(R)]
    RUTable = [[0] * C for _ in range(R)]
    LUTable = [[0] * C for _ in range(R)]
    for j in range(C):
        for i in range(R):
            if mapTable[i][j] == 1:
                if j == 0 or i == R - 1:
                    LDTable[i][j] = 1
                else:
                    LDTable[i][j] = LDTable[i + 1][j - 1] + 1 
    for j in reversed(range(C)):
        for i in range(R):
            if mapTable[i][j] == 1:
                if j == C - 1 or i == R - 1:
                    RDTable[i][j] = 1
                else:
                    RDTable[i][j] = RDTable[i + 1][j + 1] + 1 
    for j in reversed(range(C)):
        for i in range(R):
            if mapTable[i][j] == 1:
                if j == C - 1 or i == 0:
                    RUTable[i][j] = 1
                else:
                    RUTable[i][j] = RUTable[i - 1][j + 1] + 1 
    for j in range(C):
        for i in reversed(range(R)):
            if mapTable[i][j] == 1:
                if j == 0 or i == 0:
                    LUTable[i][j] = 1
                else:
                    LUTable[i][j] = LUTable[i - 1][j - 1] + 1
    #print(LDTable)
    #print(RDTable)
    #print(RUTable)
    #print(LUTable)
    for i in range(R):
        for j in range(C):
            temp = ans
            for k in range(ans + 1, maxSize + 1):
                if i - (k - 1) < 0 or i + (k - 1) >= R or j - (k - 1) < 0 or j - (k - 1) >= C:
                    break
                if LDTable[i - (k - 1)][j] >= k and RDTable[i][j - (k - 1)] >= k and RUTable[i + (k - 1)][j] >= k and LUTable[i][j + (k - 1)] >= k:
                    temp = max(ans, k)
            ans = temp
    print(ans)
    return

if __name__ == "__main__":
    main()