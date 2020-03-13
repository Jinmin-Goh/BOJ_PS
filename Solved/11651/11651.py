# Problem No.: 11651
# Solver:      Jinmin Goh
# Date:        20200313
# URL: https://www.acmicpc.net/problem/11651

import sys

def main():
    n = int(input())
    nums = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        nums.append([y, x])
    nums.sort()
    for i in nums:
        print(i[1], i[0])
    return

if __name__ == "__main__":
    main()