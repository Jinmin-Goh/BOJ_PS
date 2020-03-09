# Problem No.: 2750
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/2750

import sys

def main():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    nums.sort()
    for i in nums:
        print(i)
    return

if __name__ == "__main__":
    main()