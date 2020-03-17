# Problem No.: 1436
# Solver:      Jinmin Goh
# Date:        20200316
# URL: https://www.acmicpc.net/problem/1436

import sys

def main():
    n = int(input())
    numList = ["666"]
    while len(numList) < 10000:
        tempList = []
        for i in numList:
            for j in range(0, 10):
                tempList.append(i + str(j))
                tempList.append(str(j) + i)
        tempList = set(tempList)
        tempList = list(tempList)
        numList += tempList
        numList = set(numList)
        numList = list(numList)
    for i in range(len(numList)):
        numList[i] = int(numList[i])
    numList = list(set(numList))
    numList.sort()
    print(numList[n - 1])

    return

if __name__ == "__main__":
    main()