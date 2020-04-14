# Problem No.: 2407
# Solver:      Jinmin Goh
# Date:        20200414
# URL: https://www.acmicpc.net/problem/2407

import sys

def main():
    n, m = map(int, input().split())
    ans = 1
    mFact = 1
    diffFact = 1
    for i in range(n):
        ans *= i + 1
        if i == m - 1:
            mFact = ans
        if i == n - m - 1:
            diffFact = ans
    print(ans // (mFact * diffFact))
    return

if __name__ == "__main__":
    main()