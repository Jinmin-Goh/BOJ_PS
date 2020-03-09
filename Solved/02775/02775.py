# Problem No.: 2775
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/2775

import sys

def main():
    n = int(input())
    nums = []
    for i in range(n):
        temp = []
        temp.append(int(input()))
        temp.append(int(input()))
        nums.append(temp)
    table = [[0] * 14 for i in range(15)]
    table[0] = [i + 1 for i in range(14)]
    for i in range(1,15):
        for j in range(14):
            table[i][j] = sum(table[i - 1][:j + 1])
    for i in nums:
        print(table[i[0]][i[1] - 1])
    return

if __name__ == "__main__":
    main()