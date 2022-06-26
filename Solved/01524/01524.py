# Problem No.: 1524
# Solver:      Jinmin Goh
# Date:        20220626
# URL: https://www.acmicpc.net/problem/1524

import sys

def main():
    t = int(input())
    for _ in range(t):
        temp = sys.stdin.readline()
        n, m = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))
        if max(a) < max(b):
            print('B')
        else:
            print('S')
    return

if __name__ == "__main__":
    main()