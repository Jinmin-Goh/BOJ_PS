# Problem No.: 11868
# Solver:      Jinmin Goh
# Date:        20200511
# URL: https://www.acmicpc.net/problem/11868

import sys

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    temp = nums[0]
    for i in range(1, n):
        temp ^= nums[i]
    if temp:
        print("koosaga")
    else:
        print("cubelover")

    return

if __name__ == "__main__":
    main()