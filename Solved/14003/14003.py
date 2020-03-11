# Problem No.: 14003
# Solver:      Jinmin Goh
# Date:        20200311
# URL: https://www.acmicpc.net/problem/14003

import sys

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    dpList = []
    for i in range(n):
        #print(dpList)
        if not dpList:
            dpList.append([nums[i]])
            continue
        if len(dpList) == 1:
            if dpList[0][-1] >= nums[i]:
                dpList[0].append(nums[i])
            else:
                dpList.append([nums[i]])
        else:
            pFront = 0
            pRear = len(dpList) - 1
            while pFront < pRear < len(dpList):
                pMid = (pFront + pRear) // 2
                #print(pFront, pMid, pRear)
                if dpList[pMid][-1] < nums[i]:
                    pFront = pMid + 1
                else:
                    pRear = pMid
            #print("n:", nums[i], "final:", pFront, pMid, pRear)
            if pFront >= len(dpList) - 1:
                if dpList[-1][-1] >= nums[i]:
                    dpList[-1].append(nums[i])
                else:
                    dpList.append([nums[i]])
            else:
                dpList[pFront].append(nums[i])
    #print(dpList)
    print(len(dpList))
    ansList = []
    for i in reversed(range(len(dpList))):
        if not ansList:
            ansList.append(dpList[i][0])
        else:
            for j in dpList[i]:
                if ansList[-1] <= j:
                    continue
                else:
                    ansList.append(j)
                    break
    #print(ansList)
    for i in range(len(ansList)):
        print(ansList[-i - 1], end= " ")
    return

if __name__ == "__main__":
    main()