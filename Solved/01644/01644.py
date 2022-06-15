# Problem No.: 1644
# Solver:      Jinmin Goh
# Date:        20220615
# URL: https://www.acmicpc.net/problem/1644

import sys

def main():
    n = int(input())
    check = [False for _ in range(n + 1)]
    pList = []
    for i in range(2, n + 1):
        if not check[i]:
            pList.append(i)
            temp = i
            while temp <= n:
                check[temp] = True
                temp += i
    p1 = 0
    p2 = 0
    sumVal = 2
    pCnt = len(pList)
    ans = 0
    while p1 < pCnt and p2 < pCnt:
        if sumVal == n:
            ans += 1
            p1 += 1
            sumVal -= pList[p1 - 1]
        elif sumVal > n:
            p1 += 1
            sumVal -= pList[p1 - 1]
        else:
            p2 += 1
            if p2 >= pCnt:
                break
            sumVal += pList[p2]
    print(ans)

    return

if __name__ == "__main__":
    main()