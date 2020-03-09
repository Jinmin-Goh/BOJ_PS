# Problem No.: 2751
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/2751

import sys

def main():
    n = int(input())
    nums = []
    for i in range(n):
        temp = sys.stdin.readline().split()
        nums.append(int(temp[0]))
    nums.sort()
    for i in nums:
        print(i)
    return

if __name__ == "__main__":
    main()