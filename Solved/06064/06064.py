# Problem No.: 6064
# Solver:      Jinmin Goh
# Date:        20200610
# URL: https://www.acmicpc.net/problem/6064

import sys

def gcd(a: int, b: int) -> int:
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)
    
# naive TLE solution
def main():
    t = int(input())
    for _ in range(t):
        n, m, x, y = map(int, sys.stdin.readline().split())
        gcdVal = gcd(n, m)
        if abs(x - y) % gcdVal:
            print(-1)
            continue
        
        if n < m:
            n, m = m, n
            x, y = y, x
        ans = x - 1
        while (ans % m) != (y - 1):
            ans += n
        print(ans + 1)
    return

if __name__ == "__main__":
    main()