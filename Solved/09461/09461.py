# Problem No.: 9461
# Solver:      Jinmin Goh
# Date:        20200311
# URL: https://www.acmicpc.net/problem/9461

import sys

def main():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    dpList = [0] * 101
    for i in range(1, 101):
        if i in [1, 2, 3]:
            dpList[i] = 1
        elif i in [4, 5]:
            dpList[i] = 2
        else:
            dpList[i] = dpList[i - 1] + dpList[i - 5]
    for i in nums:
        print(dpList[i])
    return

if __name__ == "__main__":
    main()