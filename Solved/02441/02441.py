# Problem No.: 2441
# Solver:      Jinmin Goh
# Date:        20200426
# URL: https://www.acmicpc.net/problem/2441

import sys

def main():
    n = int(input())
    for i in range(n):
        print(" " * i + "*" * (n - i))
    return

if __name__ == "__main__":
    main()