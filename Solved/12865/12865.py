# Problem No.: 12865
# Solver:      Jinmin Goh
# Date:        20200428
# URL: https://www.acmicpc.net/problem/12865

import sys

# we need to construct DP table for a product usage, not for a weight.

def main():
    n, k = map(int, input().split())
    nums = []
    for i in range(n):
        a, b = map(int, sys.stdin.readline().split())
        nums.append((a, b))
    dpList = [0] * (k + 1)
    for i in range(n):
        for j in range(k, 0, -1):
            if nums[i][0] <= j:
                dpList[j] = max(dpList[j], dpList[j - nums[i][0]] + nums[i][1])
    print(dpList[-1])
    return

if __name__ == "__main__":
    main()