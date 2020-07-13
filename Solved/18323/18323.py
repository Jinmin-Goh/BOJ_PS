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

    # O(n ^ 2) solution
    for i in range(1, n + 1):
        ans = [None] * n
        numSet = set([_ + 1 for _ in range(n)])
        ans[0] = i
        numSet.remove(i)
        for j in range(1, n):
            temp = nums[j - 1] - ans[j - 1]
            if temp not in numSet:
                break
            numSet.remove(temp)
            ans[j] = temp
        if not numSet:
            break

    for i in ans:
        print(i, end = " ")

    return

if __name__ == "__main__":
    main()