# Problem No.: 11055
# Solver:      Jinmin Goh
# Date:        20200312
# URL: https://www.acmicpc.net/problem/11055

import sys

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    dpList = nums[:]
    for i in range(n):
        for j in range(i + 1):
            if nums[i] > nums[j]:
                dpList[i] = max(dpList[i], nums[i] + dpList[j])
        #print(dpList)
    print(max(dpList))
    return

if __name__ == "__main__":
    main()