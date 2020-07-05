# Problem No.: 2442
# Solver:      Jinmin Goh
# Date:        20200705
# URL: https://www.acmicpc.net/problem/2442

import sys

def main():
    n = int(input())    
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * (i - 1) + 1))
        return

if __name__ == "__main__":
    main()