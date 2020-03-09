# Problem No.: 1018
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/1018

import sys

def main():
    row, col = map(int, input().split())
    inputTable = []
    for i in range(row):
        inputTable.append(list(input()))
    costW = [[0] * col for i in range(row)]
    costB = [[0] * col for i in range(row)]
    for i in range(row):
        for j in range(col):
            if (i + j) % 2:
                if inputTable[i][j] == "W":
                    costW[i][j] = 1
                else:
                    costB[i][j] = 1
            else:
                if inputTable[i][j] == "B":
                    costW[i][j] = 1
                else:
                    costB[i][j] = 1
    ans = 2500
    for i in range(row - 7):
        for j in range(col - 7):
            tempSumW = 0
            tempSumB = 0
            for k in range(8):
                tempSumW += sum(costW[i + k][j:j + 8])
                tempSumB += sum(costB[i + k][j:j + 8])
            ans = min(ans, tempSumW, tempSumB)
    print(ans)          
    return

if __name__ == "__main__":
    main()