# Problem No.: 12920
# Solver:      Jinmin Goh
# Date:        20200428
# URL: https://www.acmicpc.net/problem/12920

import sys

def main():
    n, k = map(int, input().split())
    nums = []
    for i in range(n):
        a, b, c = map(int, sys.stdin.readline().split())
        temp = 1
        # group the items with k, 2k, 4k, ... and remainder
        while 2 * temp - 1 <= c:
            nums.append((a * temp, b * temp))
            temp <<= 1
        # remainder
        nums.append((a * (c - temp + 1), b * (c - temp + 1)))
    dpList = [0] * (k + 1)
    for i in range(len(nums)):
        for j in range(k, 0, -1):
            if nums[i][0] <= j:
                dpList[j] = max(dpList[j], dpList[j - nums[i][0]] + nums[i][1])
            else:
                break
    print(dpList[-1])
    return

if __name__ == "__main__":
    main()