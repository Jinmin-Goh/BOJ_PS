# Problem No.: 2475
# Solver:      Jinmin Goh
# Date:        20200308
# URL: https://www.acmicpc.net/problem/2475

import sys

def main():
    nums = input().split()
    ans = 0
    for i in nums:
        ans += int(i) ** 2
    print(ans % 10)

if __name__ == "__main__":
    main()