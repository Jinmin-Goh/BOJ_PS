# Problem No.: 16895
# Solver:      Jinmin Goh
# Date:        20200512
# URL: https://www.acmicpc.net/problem/16895

import sys

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    xorList = [0] * n
    temp = 0
    for i in range(n - 1):
        temp ^= nums[i]
        xorList[i + 1] = temp
    temp = 0
    for i in reversed(range(1, n)):
        temp ^= nums[i]
        xorList[i - 1] ^= temp
    
    if xorList[0] ^ nums[0] == 0:
        print(0)
    else:
        ans = 0
        for i in range(n):
            if xorList[i] <= nums[i]:
                ans += 1
        print(ans)
    return

if __name__ == "__main__":
    main()