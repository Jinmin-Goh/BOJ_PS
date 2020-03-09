# Problem No.: 10816
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/10816

import sys

def main():
    n = int(input())
    nList = map(int, input().split())
    m = int(input())
    mList = map(int, input().split())
    numDict = {}
    for i in nList:
        if i not in numDict:
            numDict[i] = 1
        else:
            numDict[i] += 1
    for i in mList:
        if i in numDict:
            print(numDict[i], end=" ")
        else:
            print(0, end=" ")
    return

if __name__ == "__main__":
    main()