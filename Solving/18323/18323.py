# Problem No.: 18323
# Solver:      Jinmin Goh
# Date:        20200710
# URL: https://www.acmicpc.net/problem/18323

import sys

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))

    # b_i = a_i + a_(i + 1)
    # b is given, regenerate permutation a

    # backtracking
    for i in range(n - 1):
        nums[i] = (i, nums[i])
    nums.sort()
    ans = [None] * n
    

    return

if __name__ == "__main__":
    main()