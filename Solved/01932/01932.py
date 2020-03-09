# Problem No.: 1932
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/1932

import sys

def main():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(list(map(int, input().split())))
    cost = [nums[0][0]]
    for i in range(1, n):
        temp = []
        for j in range(i + 1):
            if j == 0:
                temp.append(nums[i][0] + cost[0])
            elif j == i:
                temp.append(nums[i][-1] + cost[-1])
            else:
                temp.append(nums[i][j] + max(cost[j], cost[j - 1]))
        cost = temp[:]
    print(max(cost))
    return

if __name__ == "__main__":
    main()