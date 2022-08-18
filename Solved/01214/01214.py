# Problem No.: 1214
# Solver:      Jinmin Goh
# Date:        20220817
# URL: https://www.acmicpc.net/problem/1214

import sys

def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    return gcd(b, a % b)

def main():
    d, p, q = map(int, sys.stdin.readline().split())
    if d % p == 0 or d % q == 0:
        print(d)
        return
    if p > q:
        p, q = q, p
    ans = ((d // p) + 1) * p
    cnt = (d // p) + 1
    val = ans
    for _ in range(1, q // gcd(p, q)):
        val += q
        cnt -= (val - d) // p
        if cnt <= 0:
            val -= (cnt + (val - d) // p) * p
            ans = min(ans, val)
            break
        else:
            val -= ((val - d) // p) * p
            ans = min(ans, val)
    print(ans)
    return

if __name__ == "__main__":
    main()