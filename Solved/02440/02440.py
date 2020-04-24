# Problem No.: 2440
# Solver:      Jinmin Goh
# Date:        20200425
# URL: https://www.acmicpc.net/problem/2440

import sys

def main():
    n = int(input())
    for i in reversed(range(n)):
        print("*" * (i + 1))
    return

if __name__ == "__main__":
    main()