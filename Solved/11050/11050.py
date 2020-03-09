# Problem No.: 11050
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/11050

import sys

def main():
    n, k = map(int, input().split())
    if k == 0:
        print(1)
        return
    ans = 1
    for i in range(k):
        ans *= (n - i)
    for i in range(k):
        ans = ans // (i + 1)
    print(ans)
    return

if __name__ == "__main__":
    main()