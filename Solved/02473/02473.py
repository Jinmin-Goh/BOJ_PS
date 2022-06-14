# Problem No.: 2473
# Solver:      Jinmin Goh
# Date:        20220614
# URL: https://www.acmicpc.net/problem/2473

import sys

def main():
    n = int(input())
    nList = list(input().split())
    for i in range(n):
        nList[i] = int(nList[i])
    nList.sort()
    ans = [0, 1, n - 1]
    minVal = nList[0] + nList[1] + nList[n - 1]
    for p in range(n - 2):
        p1 = p + 1
        p2 = n - 1
        if abs(minVal) > abs(nList[p] + nList[p1] + nList[p2]):
            minVal = nList[p] + nList[p1] + nList[p2]
            ans = [p, p1, p2]
        while p1 + 1 < p2:
            val1 = nList[p] + nList[p1 + 1] + nList[p2]
            val2 = nList[p] + nList[p1] + nList[p2 - 1]
            if abs(minVal) > abs(val1) or abs(minVal) > abs(val2):
                if abs(val1) < abs(val2):
                    ans = [p, p1 + 1, p2]
                    minVal = val1
                    p1 += 1
                else:
                    ans = [p, p1, p2 - 1]
                    minVal = val2
                    p2 -= 1
            else:
                if abs(val1) < abs(val2):
                    p1 += 1
                else:
                    p2 -= 1
    print(nList[ans[0]], nList[ans[1]], nList[ans[2]])
    return

if __name__ == "__main__":
    main()