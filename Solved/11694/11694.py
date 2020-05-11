# Problem No.: 11694
# Solver:      Jinmin Goh
# Date:        20200512
# URL: https://www.acmicpc.net/problem/11694

import sys

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    temp = nums[0]
    oneCnt = 0
    if nums[0] == 1:
        oneCnt += 1
    for i in range(1, n):
        temp ^= nums[i]
        if nums[i] == 1:
            oneCnt += 1
    if oneCnt == n:
        if oneCnt % 2:
            print("cubelover")
        else:
            print("koosaga")
    else:
        if temp:
            print("koosaga")
        else:
            print("cubelover")
    return

if __name__ == "__main__":
    main()