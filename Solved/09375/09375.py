# Problem No.: 9375
# Solver:      Jinmin Goh
# Date:        20200413
# URL: https://www.acmicpc.net/problem/9375

import sys

def main():
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        wearDict = {}
        for i in range(n):
            a, b = sys.stdin.readline().split()
            if b not in wearDict:
                wearDict[b] = 1
            else:
                wearDict[b] += 1
        ans = 1
        for i in wearDict:
            ans *= wearDict[i] + 1
        print(ans - 1)
    return

if __name__ == "__main__":
    main()