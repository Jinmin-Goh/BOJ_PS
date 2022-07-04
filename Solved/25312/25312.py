# Problem No.: 25312
# Solver:      Jinmin Goh
# Date:        20220704
# URL: https://www.acmicpc.net/problem/25312

import sys

def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def main():
    n, m = map(int, input().split())
    juice = []
    for _ in range(n):
        w, v = map(int, sys.stdin.readline().split())
        juice.append((v / w, w, v))
    juice.sort()
    p = n - 1
    ans = 0
    while p >= 0 and juice[p][1] <= m:
        m -= juice[p][1]
        ans += juice[p][2]
        p -= 1
    if m == 0:
        print(f"{ans}/1")
    else:
        val = gcd(juice[p][1], m)
        a = m // val
        b = juice[p][1] // val
        a = a * juice[p][2] + b * ans
        val = gcd(a, b)
        a //= val
        b //= val
        print(f"{a}/{b}")

    return

if __name__ == "__main__":
    main()