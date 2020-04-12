# Problem No.: 17219
# Solver:      Jinmin Goh
# Date:        20200413
# URL: https://www.acmicpc.net/problem/17219

import sys

def main():
    n, m = map(int, input().split())
    passwordDict = {}
    for _ in range(n):
        a, b = sys.stdin.readline().split()
        passwordDict[a] = b
    for _ in range(m):
        print(passwordDict[sys.stdin.readline().strip()])
    return

if __name__ == "__main__":
    main()