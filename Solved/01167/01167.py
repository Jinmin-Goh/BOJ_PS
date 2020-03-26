# Problem No.: 1167
# Solver:      Jinmin Goh
# Date:        20200326
# URL: https://www.acmicpc.net/problem/1167

import sys

def main():
    n = int(input())
    graphList = {i:[] for i in range(1, n + 1)}
    for _ in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        cnt = 1
        while temp[cnt] != -1:
            graphList[temp[0]].append((temp[cnt], temp[cnt + 1]))
            cnt += 2
    stack = [[1, 0]]
    usedSet = set()
    maxVal = [1, 0]
    while stack:
        temp = []
        #print(stack, usedSet)
        for i in stack:
            tempList = graphList[i[0]]
            for j in tempList:
                if j[0] not in usedSet:
                    temp.append([j[0], i[1] + j[1]])
                    if maxVal[1] < i[1] + j[1]:
                        maxVal = [j[0], i[1] + j[1]]
            usedSet.add(i[0])
        stack = temp[:]
    #print(maxVal)
    usedSet = set()
    maxVal = [maxVal[0], 0]
    stack = [maxVal[:]]
    while stack:
        temp = []
        #print(stack, usedSet)
        for i in stack:
            tempList = graphList[i[0]]
            for j in tempList:
                if j[0] not in usedSet:
                    temp.append([j[0], i[1] + j[1]])
                    if maxVal[1] < i[1] + j[1]:
                        maxVal = [j[0], i[1] + j[1]]
            usedSet.add(i[0])
        stack = temp[:]
    print(maxVal[1])

    return

if __name__ == "__main__":
    main()