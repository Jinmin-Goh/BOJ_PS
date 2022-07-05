# Problem No.: 2042
# Solver:      Jinmin Goh
# Date:        20220705
# URL: https://www.acmicpc.net/problem/2042

import sys

def update(arr, idx, val, node, l, r):
    if idx <= l and r <= idx:
        arr[node] = val
        return
    elif idx < l or r < idx:
        return
    m = (l + r) // 2
    update(arr, idx, val, node * 2, l, m)
    update(arr, idx, val, node * 2 + 1, m + 1, r)
    arr[node] = arr[node * 2] + arr[node * 2 + 1]
    return 

def print_sum(arr, ql, qr, node, l, r):
    if ql <= l and r <= qr:
        return arr[node]
    elif qr < l or r < ql:
        return 0
    m = (l + r) // 2
    l_val = print_sum(arr, ql, qr, node * 2, l, m)
    r_val = print_sum(arr, ql, qr, node * 2 + 1, m + 1, r)
    return l_val + r_val

def main():
    n, m, k = map(int, input().split())
    arr = [0 for _ in range(4 * n + 1)]
    for i in range(n):
        update(arr, i + 1, int(sys.stdin.readline()), 1, 1, n)
    for _ in range(m + k):
        q, a, b = map(int, sys.stdin.readline().split())
        if q == 1:
            update(arr, a, b, 1, 1, n)
        elif q == 2:
            if a > b:
                a, b = b, a
            print(print_sum(arr, a, b, 1, 1, n))
    return

if __name__ == "__main__":
    main()