# Problem No.: 9095
# Solver:      Jinmin Goh
# Date:        20200306
# URL: https://www.acmicpc.net/problem/9095

import sys

def DP(n: int, dpList: [int]):
    if not dpList[n]:
        dpList[n] = dpList[n - 1] + dpList[n - 2] + dpList[n - 3]
    return dpList[n]

def main():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    dpList = [0] * 11
    dpList[1] = 1
    dpList[2] = 2
    dpList[3] = 4
    for i in range(4, 11):
        dpList[i] = DP(i, dpList)
    for i in nums:
        print(dpList[i])

if __name__ == "__main__":
    main()