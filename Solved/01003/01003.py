# Problem No.: 1003
# Solver:      Jinmin Goh
# Date:        20200307
# URL: https://www.acmicpc.net/problem/1003

import sys

def fb(n: int, dpList: [(int, int)]) -> (int, int):
    if n == 0 or n == 1:
        return dpList[n]
    if dpList[n][0] == -1:
        temp1 = fb(n - 1, dpList)
        temp2 = fb(n - 2, dpList)
        dpList[n] = (temp1[0] + temp2[0], temp1[1] + temp2[1])
    return dpList[n]

def main():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    maxVal = 50
    dpList = [(-1, -1)] * (maxVal + 1)
    dpList[0] = (1, 0)
    dpList[1] = (0, 1)
    fb(maxVal, dpList)
    for i in nums:
        print(dpList[i][0],dpList[i][1])

if __name__ == "__main__":
    main()