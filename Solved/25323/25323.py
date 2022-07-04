# Problem No.: 25323
# Solver:      Jinmin Goh
# Date:        20220704
# URL: https://www.acmicpc.net/problem/25323

import sys
import math

def check(n1, n2):
    n = n1 * n2
    if n == math.isqrt(n) ** 2:
        return True
    else:
        return False

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    nums_sorted = nums[:]
    nums_sorted.sort()
    ans = "YES"
    for i in range(n):
        if not check(nums[i], nums_sorted[i]):
            ans = "NO"
            break
    print(ans)
    return

if __name__ == "__main__":
    main()