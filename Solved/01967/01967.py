# Problem No.: 1967
# Solver:      Jinmin Goh
# Date:        20200327
# URL: https://www.acmicpc.net/problem/1967

import sys

def main():
    n = int(input())
    graphList = {i:[] for i in range(1, n + 1)}
    for _ in range(n - 1):
        temp = list(map(int, sys.stdin.readline().split()))
        graphList[temp[0]].append((temp[1],temp[2]))
        graphList[temp[1]].append((temp[0],temp[2]))
    #print(graphList)
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