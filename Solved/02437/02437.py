# Problem No.: 2437
# Solver:      Jinmin Goh
# Date:        20200326
# URL: https://www.acmicpc.net/problem/2437

import sys

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    ans = 0
    for i in nums:
        if i > ans + 1:
            break
        ans += i
    print(ans + 1)
    return

if __name__ == "__main__":
    main()