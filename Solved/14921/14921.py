# Problem No.: 14921
# Solver:      Jinmin Goh
# Date:        20220614
# URL: https://www.acmicpc.net/problem/14921

import sys

def main():
    n = int(input())
    nList = list(input().split())
    for i in range(n):
        nList[i] = int(nList[i])
    nList.sort()
    p1 = 0
    p2 = n - 1
    minVal = nList[p1] + nList[p2]
    while p1 + 1 < p2:
        val1 = nList[p1 + 1] + nList[p2]
        val2 = nList[p1] + nList[p2 - 1]
        if abs(minVal) > abs(val1) or abs(minVal) > abs(val2):
            if abs(val1) < abs(val2):
                minVal = val1
                p1 += 1
            else:
                minVal = val2
                p2 -= 1
        else:
            if abs(val1) < abs(val2):
                p1 += 1
            else:
                p2 -= 1
    print(minVal)
    return

if __name__ == "__main__":
    main()