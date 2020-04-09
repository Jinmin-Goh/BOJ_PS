# Problem No.: 11399
# Solver:      Jinmin Goh
# Date:        20200410
# URL: https://www.acmicpc.net/problem/11399

import sys

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    ans = 0
    temp = 0
    for i in nums:
        ans += temp + i
        temp += i
    print(ans)
    return

if __name__ == "__main__":
    main()