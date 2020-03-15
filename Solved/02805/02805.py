# Problem No.: 2805
# Solver:      Jinmin Goh
# Date:        20200315
# URL: https://www.acmicpc.net/problem/2805

import sys

def main():
    n, m = map(int, input().split())
    treeList = list(map(int, sys.stdin.readline().split()))
    treeDict = {}
    for i in treeList:
        if i not in treeDict:
            treeDict[i] = 1
        else:
            treeDict[i] += 1
    maxHeight = max(treeDict)
    pFront = 0
    pRear = maxHeight
    while pFront < pRear:
        pMid = (pFront + pRear) // 2
        #print(pFront, pMid, pRear)
        if pMid == pFront:
            break
        tempSum = 0
        for i in treeDict:
            tempSum += max(0, i - pMid) * treeDict[i]
        #print(tempSum)
        if tempSum < m:
            pRear = pMid
        else:
            pFront = pMid
    print(pMid)
    return

if __name__ == "__main__":
    main()