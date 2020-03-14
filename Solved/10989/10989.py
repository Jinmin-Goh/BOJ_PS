# Problem No.: 10989
# Solver:      Jinmin Goh
# Date:        20200314
# URL: https://www.acmicpc.net/problem/10989

import sys

def main():
    n = int(input())
    numDict = {}
    for i in range(n):
        temp = int(sys.stdin.readline())
        if temp not in numDict:
            numDict[temp] = 1
        else:
            numDict[temp] += 1
    nums = list(numDict.keys())
    nums.sort()
    for i in nums:
        for j in range(numDict[i]):
            print(i)
    return

if __name__ == "__main__":
    main()