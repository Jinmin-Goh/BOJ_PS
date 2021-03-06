# Problem No.: 11722
# Solver:      Jinmin Goh
# Date:        20200312
# URL: https://www.acmicpc.net/problem/11722

import sys

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    temp = []
    while nums:
        temp.append(nums.pop())
    nums = temp
    dpList = []
    for i in range(n):
        if not dpList:
            dpList.append(nums[i])
            continue
        if len(dpList) == 1:
            if dpList[0] >= nums[i]:
                dpList[0] = nums[i]
            else:
                dpList.append(nums[i])
        else:
            pFront = 0
            pRear = len(dpList) - 1
            while pFront < pRear < len(dpList):
                pMid = (pFront + pRear) // 2
                #print(pFront, pMid, pRear)
                if dpList[pMid] < nums[i]:
                    pFront = pMid + 1
                else:
                    pRear = pMid
            #print("n:", nums[i], "final:", pFront, pMid, pRear)
            if pFront >= len(dpList) - 1:
                if dpList[-1] >= nums[i]:
                    dpList[-1] = nums[i]
                else:
                    dpList.append(nums[i])
            else:
                dpList[pFront] = nums[i]
    print(len(dpList))
    return

if __name__ == "__main__":
    main()