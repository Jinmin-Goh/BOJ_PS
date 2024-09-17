# Problem No.: 25372
# Solver:      Jinmin Goh
# Date:        20220913
# URL: https://www.acmicpc.net/problem/25372

import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        p = sys.stdin.readline().rstrip()
        if 6 <= len(p) <= 9:
            print("yes")
        else:
            print("no")
    return

if __name__ == "__main__":
    main()