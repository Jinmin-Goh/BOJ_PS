# Problem No.: 5525
# Solver:      Jinmin Goh
# Date:        20200608
# URL: https://www.acmicpc.net/problem/5525

import sys
# TLE, O(n ^ 2) solution
def main():
    n = int(input())
    m = int(input())
    s = sys.stdin.readline().strip()
    temp = "I" + "OI" * n
    pFront = 0
    pRear = 0
    ans = 0
    while pRear < m and pFront < m:
        while pRear < m and pRear - pFront < 2 * n and s[pRear] == temp[pRear - pFront]:
            pRear += 1
        if pRear < m and pRear - pFront == 2 * n and s[pRear] == temp[pRear - pFront]:
            ans += 1
            if pRear + 2 < m and s[pRear + 1] == "O" and s[pRear + 2] == "I":
                pRear += 2
                pFront += 2
            else:
                pFront = pRear + 1
                pRear = pFront
        else:
            pFront += 1
            pRear = pFront
    print(ans)
    return

if __name__ == "__main__":
    main()