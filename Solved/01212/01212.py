# Problem No.: 1212
# Solver:      Jinmin Goh
# Date:        20220618
# URL: https://www.acmicpc.net/problem/1212

import sys

def main():
    n = int(input(), 8)
    ans = bin(n)
    print(ans[2:])
    return

if __name__ == "__main__":
    main()