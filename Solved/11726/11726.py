# Problem No.: 11726
# Solver:      Jinmin Goh
# Date:        20200307
# URL: https://www.acmicpc.net/problem/11726

import sys

def DP(n: int, dpList: [int]) -> int:
    if n == 1 or n == 2:
        return dpList[n]
    if dpList[n] == -1:
        dpList[n] = (DP(n - 1, dpList) + DP(n - 2, dpList)) % 10007
    return dpList[n]

def main():
    n = int(input())
    if n == 1:
        print(1)
        return
    dpList = [-1] * (n + 1)
    dpList[1] = 1
    dpList[2] = 2
    for i in range(1, n + 1):
        DP(i, dpList)
    print(dpList[n])


if __name__ == "__main__":
    main()    