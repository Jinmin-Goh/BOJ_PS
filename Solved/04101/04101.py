# Problem No.: 4101
# Solver:      Jinmin Goh
# Date:        20220907
# URL: https://www.acmicpc.net/problem/4101

import sys

def main():
    a, b = map(int, sys.stdin.readline().split())
    while a and b:
        print("Yes" if a > b else "No")
        a, b = map(int, sys.stdin.readline().split())
    return

if __name__ == "__main__":
    main()