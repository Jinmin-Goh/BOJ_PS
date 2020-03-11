# Problem No.: 11053
# Solver:      Jinmin Goh
# Date:        20200311
# URL: https://www.acmicpc.net/problem/11053

# time: O(n^2)

import sys

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    dpList = [1] * n
    ans = 1
    for i in range(1, n):
        maxVal = 0
        for j in range(i):
            if nums[i] > nums[j]:
                maxVal = max(maxVal, dpList[j])
        dpList[i] = maxVal + 1
        ans = max(ans, dpList[i])
    print(ans)
    return

if __name__ == "__main__":
    main()