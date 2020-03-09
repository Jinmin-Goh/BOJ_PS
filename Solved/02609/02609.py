# Problem No.: 2609
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/2609

import sys

def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a
    gcdVal = gcd(a, b)
    print(gcdVal)
    print(a * b // gcdVal)
    return

if __name__ == "__main__":
    main()