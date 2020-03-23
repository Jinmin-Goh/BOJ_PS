# Problem No.: 1539
# Solver:      Jinmin Goh
# Date:        20200323
# URL: https://www.acmicpc.net/problem/1539

import sys
import bisect

def main():
    n = int(input())
    ans = 0
    nums = []
    for _ in range(n):
        x = int(sys.stdin.readline())
        #print(nums)
        if not nums:
            nums.append((x, 1))
            ans += 1
            continue
        if x > nums[-1][0]:
            nums.append((x, nums[-1][1] + 1))
            continue
        #pFront = 0
        #pRear = len(nums) - 1
        #while pFront < pRear:
        #    pMid = (pFront + pRear) // 2
        #    if nums[pMid][0] >= x:
        #        pRear = pMid
        #    else:
        #        pFront = pMid + 1
        pFront = bisect.bisect(nums, (x, n))
        ans += max(nums[pFront][1], nums[pFront - 1][1]) + 1
        bisect.insort(nums, (x, max(nums[pFront][1], nums[pFront - 1][1]) + 1))
    print(ans)
    return

if __name__ == "__main__":
    main()