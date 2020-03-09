# Problem No.: 2231
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/2231

import sys

def main():
    n = int(input())
    length = len(str(n))
    for i in range(max(1,n - 9 * length), n + 9 * length + 1):
        tempStr = str(i)
        tempSum = 0
        for j in tempStr:
            tempSum += int(j)
        sumVal = tempSum + i
        if sumVal == n:
            print(i)
            return
    print(0)

if __name__ == "__main__":
    main()