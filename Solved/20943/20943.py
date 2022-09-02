# Problem No.: 20943
# Solver:      Jinmin Goh
# Date:        20220902
# URL: https://www.acmicpc.net/problem/20943

import sys

def gcd(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    return gcd(b, a % b)

def main():
    n = int(sys.stdin.readline().rstrip())
    lines = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    ratio = {}
    flag = True
    for a, b, _ in lines:
        if a == 0 or b == 0:
            if a == 0:
                if 'a_zero' not in ratio:
                    ratio['a_zero'] = 0
                ratio['a_zero'] += 1
            if b == 0:
                if 'b_zero' not in ratio:
                    ratio['b_zero'] = 0
                ratio['b_zero'] += 1
        else:
            val = gcd(a, b)
            a //= val
            b //= val
            if a < 0:
                a, b = -a, -b
            if (a, b) not in ratio:
                ratio[(a, b)] = 0
            ratio[(a, b)] += 1
    ans = n ** 2
    for val in ratio.values():
        ans -= val ** 2
    print(ans // 2)
    return

if __name__ == "__main__":
    main()