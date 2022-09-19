# Problem No.: 25261
# Solver:      Jinmin Goh
# Date:        20220919
# URL: https://www.acmicpc.net/problem/25261

import sys

def main():
    n, k0 = map(int, sys.stdin.readline().split())
    flag = False
    for _ in range(n):
        a, b = map(str, sys.stdin.readline().split())
        a_val = int(a[1:])
        b_val = int(b[1:])
        if a[0] == '+':
            if b[0] == '+':
               k0 += max(a_val, b_val)
            elif b[0] == '*':
                if b_val == 0:
                    k0 += a_val
                elif flag:
                    if b_val == 1:
                        k0 += a_val
                    else:
                        k0 *= b_val
                else:
                    if k0 + a_val > k0 * b_val:
                        k0 += a_val
                    else:
                        k0 *= b_val
            elif b[0] == '-':
                k0 += a_val
        elif a[0] == '*':
            if b[0] == '+':
                if a_val == 0:
                    k0 += b_val
                elif flag:
                    if a_val == 1:
                        k0 += b_val
                    else:
                        k0 *= a_val
                else:
                    if k0 * a_val > k0 + b_val:
                        k0 *= a_val
                    else:
                        k0 += b_val
            elif b[0] == '*':
                if a_val == 0 and b_val == 0:
                    flag = False
                    k0 = 0
                else:
                    k0 *= max(a_val, b_val)
            elif b[0] == '-':
                if a_val == 0:
                    k0 -= b_val
                else:
                    k0 *= a_val
        elif a[0] == '-':
            if b[0] == '+':
                k0 += b_val
            elif b[0] == '*':
                if b_val == 0:
                    k0 -= a_val
                else:
                    k0 *= b_val
            elif b[0] == '-':
                k0 -= min(a_val, b_val)
        k0 = max(0, k0)
        if k0 >= 1000000007 ** 2:
            flag = True
        k0 %= 1000000007 ** 2
    print(k0 % 1000000007)
    return

if __name__ == "__main__":
    main()