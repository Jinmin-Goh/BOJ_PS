# Problem No.: 2164
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/2164

import sys

def main():
    n = int(input())
    nums = [True for i in range(n)]
    cnt = 0
    i = 0
    delFlag = True
    while cnt < n - 1:
        if nums[i]:
            if delFlag:
                nums[i] = False
                cnt += 1
                delFlag = False
            else:
                delFlag = True
        i = (i + 1) % n
    print(nums.index(True) + 1)
    return

if __name__ == "__main__":
    main()