# Problem No.: 18111
# Solver:      Jinmin Goh
# Date:        20200315
# URL: https://www.acmicpc.net/problem/18111

import sys

def main():
    n, m, b = map(int, input().split())
    mapHeight = []
    heightDict = {}
    for i in range(n):
        mapHeight.append(list(map(int, sys.stdin.readline().split())))
        for j in mapHeight[-1]:
            if j not in heightDict:
                heightDict[j] = 1
            else:
                heightDict[j] += 1
    maxHeight = max(heightDict)
    minHeight = min(heightDict)
    #print(minHeight, maxHeight, heightDict)
    cost = [2 ** 31 - 1, 0]
    for i in range(minHeight, maxHeight + 1):
        tempCost = 0
        tempB = b
        for j in heightDict:
            if j > i:
                tempB += heightDict[j] * (j - i)
                tempCost += 2 * heightDict[j] * (j - i)
            elif j < i:
                tempB -= heightDict[j] * (i - j)
                tempCost += heightDict[j] * (i - j)
            #print(i, j, tempB)
        #print(tempCost, tempB)
        if tempB < 0:
            continue
        if i > 256:
            continue
        if cost[0] > tempCost:
            cost[0] = tempCost
            cost[1] = i
        elif cost[0] == tempCost and cost[1] < i:
            cost[1] = i
        #print(cost)
    print(cost[0], cost[1])
    return

if __name__ == "__main__":
    main()