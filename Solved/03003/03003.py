# Problem No.: 3003
# Solver:      Jinmin Goh
# Date:        20220706
# URL: https://www.acmicpc.net/problem/3003

import sys

def main():
    a, b, c, d, e, f = map(int, input().split())
    a = 1 - a
    b = 1 - b
    c = 2 - c
    d = 2 - d
    e = 2 - e
    f = 8 - f
    print(a, b, c, d, e, f)
    return

if __name__ == "__main__":
    main()