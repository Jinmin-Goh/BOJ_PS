# Problem No.: 11505
# Solver:      Jinmin Goh
# Date:        20220707
# URL: https://www.acmicpc.net/problem/11505

import sys

sys.setrecursionlimit(10 ** 5)

arr = [0 for _ in range(4000001)]

def update(idx, val, n, l, r):
    if idx <= l and r <= idx:
        arr[n] = val
        return
    elif idx < l or r < idx:
        return
    m = (l + r) // 2
    update(idx, val, 2 * n, l, m)
    update(idx, val, 2 * n + 1, m + 1, r)
    arr[n] = (arr[2 * n] * arr[2 * n + 1]) % 1000000007
    return

def print_mul(ql, qr, n, l, r):
    if ql <= l and r <= qr:
        return arr[n]
    elif qr < l or r < ql:
        return 1
    m = (l + r) // 2
    l_val = print_mul(ql, qr, 2 * n, l, m)
    r_val = print_mul(ql, qr, 2 * n + 1, m + 1, r)
    return (l_val * r_val) % 1000000007

def main():
    n, m, k = map(int, input().split())
    for i in range(n):
        update(i + 1, int(sys.stdin.readline()), 1, 1, n)
    for _ in range(m + k):
        q, a, b = map(int, sys.stdin.readline().split())
        if q == 1:
            update(a, b, 1, 1, n)
        elif q == 2:
            print(print_mul(a, b, 1, 1, n))
    return

if __name__ == "__main__":
    main()