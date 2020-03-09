# Problem No.: 2869
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/2869

import sys

def main():
    a, b, v = map(int, input().split())
    if a == v:
        print(1)
        return
    delta = a - b
    ans = 0
    if (v - a) % delta:
        ans = (v - a) // delta + 2
    else:
        ans = (v - a) // delta + 1
    print(ans)
    return

if __name__ == "__main__":
    main()