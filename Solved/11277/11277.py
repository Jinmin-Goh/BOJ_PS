# Problem No.: 11277
# Solver:      Jinmin Goh
# Date:        20200515
# URL: https://www.acmicpc.net/problem/11277

import sys

def main():
    n, m = map(int, input().split())
    numList = []
    for _ in range(m):
        temp = list(map(int, input().split()))
        numList.append(temp)
    cnt = [False] * n
    for i in range(2 ** n):
        temp = True
        for j in numList:
            a = cnt[abs(j[0]) - 1]
            b = cnt[abs(j[1]) - 1]
            if j[0] < 0:
                a = not a 
            if j[1] < 0:
                b = not b
            temp = temp and (a or b)
            if not temp:
                break
        if temp:
            print(1)
            return
        tempCnt = 0
        while tempCnt < n:
            cnt[tempCnt] = not cnt[tempCnt]
            if not cnt[tempCnt]:
                tempCnt += 1
            else:
                break

    print(0)
    return

if __name__ == "__main__":
    main()