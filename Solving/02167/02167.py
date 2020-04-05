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
    print(nums, dpTable)
    k = int(input())
    for _ in range(k):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        ans = 0
        if x1 - 1 == 0:
            for i in range(y1 - 1, y2):
                ans += dpTable[x2 - 1][i] - dpTable[x1 - 2][i]
                print(ans)
            print(ans)
        else:
            for i in range(y1 - 1, y2):
                ans += dpTable[0][i]
                print(ans)
            print(ans)
    return

if __name__ == "__main__":
    main()