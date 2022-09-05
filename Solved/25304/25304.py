# Problem No.: 25304
# Solver:      Jinmin Goh
# Date:        20220905
# URL: https://www.acmicpc.net/problem/25304

import sys

def main():
    x = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    cost = 0
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        cost += a * b
    if cost == x:
        print("Yes")
    else:
        print("No")
    return

if __name__ == "__main__":
    main()