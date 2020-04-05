# Problem No.: 2167
# Solver:      Jinmin Goh
# Date:        20200405
# URL: https://www.acmicpc.net/problem/2167

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    nums = []
    for _ in range(n):
        nums.append(list(map(int, sys.stdin.readline().split())))
    dpTable = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if j == 0:
                dpTable[i][j] = nums[i][j]
            else:
                dpTable[i][j] = nums[i][j] + dpTable[i][j - 1]
    #print(nums, dpTable)
    k = int(input())
    for _ in range(k):
        r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
        ans = 0
        if c1 - 1 != 0:
            for i in range(r1 - 1, r2):
                ans += (dpTable[i][c2 - 1] - dpTable[i][c1 - 2])
                #print(ans)
            print(ans)
        else:
            for i in range(r1 - 1, r2):
                ans += dpTable[i][c2 - 1]
                #print(ans)
            print(ans)
    return

if __name__ == "__main__":
    main()