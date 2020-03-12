# Problem No.: 11054
# Solver:      Jinmin Goh
# Date:        20200312
# URL: https://www.acmicpc.net/problem/11054

import sys

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    revNums = [nums[-i - 1] for i in range(n)]
    ans = 0
    for i in range(n):
        # LIS
        incDpList = []
        for j in range(i + 1):
            #print(incDpList)
            if not incDpList:
                incDpList.append(nums[j])
                continue
            if len(incDpList) == 1:
                if incDpList[0] >= nums[j]:
                    incDpList[0] = nums[j]
                else:
                    incDpList.append(nums[j])
            else:
                pFront = 0
                pRear = len(incDpList) - 1
                while pFront < pRear < len(incDpList):
                    pMid = (pFront + pRear) // 2
                    #print(pFront, pMid, pRear)
                    if incDpList[pMid] < nums[j]:
                        pFront = pMid + 1
                    else:
                        pRear = pMid
                #print("n:", nums[j], "final:", pFront, pMid, pRear)
                if pFront >= len(incDpList) - 1:
                    if incDpList[-1] >= nums[j]:
                        incDpList[-1] = nums[j]
                    else:
                        incDpList.append(nums[j])
                else:
                    incDpList[pFront] = nums[j]
        # DIS
        decDpList = []
        for j in range(len(nums) - i):
            #print(decDpList)
            if not decDpList:
                decDpList.append(revNums[j])
                continue
            if len(decDpList) == 1:
                if decDpList[0] >= revNums[j]:
                    decDpList[0] = revNums[j]
                else:
                    decDpList.append(revNums[j])
            else:
                pFront = 0
                pRear = len(decDpList) - 1
                while pFront < pRear < len(decDpList):
                    pMid = (pFront + pRear) // 2
                    #print(pFront, pMid, pRear)
                    if decDpList[pMid] < revNums[j]:
                        pFront = pMid + 1
                    else:
                        pRear = pMid
                #print("n:", revNums[j], "final:", pFront, pMid, pRear)
                if pFront >= len(decDpList) - 1:
                    if decDpList[-1] >= revNums[j]:
                        decDpList[-1] = revNums[j]
                    else:
                        decDpList.append(revNums[j])
                else:
                    decDpList[pFront] = revNums[j]
        ans = max(ans, len(incDpList) + len(decDpList) - 1)
    print(ans)
    return

if __name__ == "__main__":
    main()