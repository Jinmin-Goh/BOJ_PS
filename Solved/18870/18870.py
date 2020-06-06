# Problem No.: 18870
# Solver:      Jinmin Goh
# Date:        20200606
# URL: https://www.acmicpc.net/problem/18870

import sys

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    uniqNum = list(set(nums))
    uniqNum.sort()
    ans = []
    for i in range(n):
        num = nums[i]
        pFront = 0
        pRear = len(uniqNum) - 1
        if uniqNum[pFront] == num:
            ans.append(pFront)
            continue
        if uniqNum[pRear] == num:
            ans.append(pRear)
            continue
        while pFront < pRear:
            pMid = (pFront + pRear) // 2
            if uniqNum[pFront] == num:
                ans.append(pFront)
                break
            if uniqNum[pRear] == num:
                ans.append(pRear)
                break
            if uniqNum[pMid] > num:
                pRear = pMid - 1
            elif uniqNum[pMid] < num:
                pFront = pMid + 1
            else:
                ans.append(pMid)
                break
    
    for i in range(n):
        print(ans[i], end = " ")

    return

if __name__ == "__main__":
    main()