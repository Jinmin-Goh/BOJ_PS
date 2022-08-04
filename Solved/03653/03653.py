# Problem No.: 3653
# Solver:      Jinmin Goh
# Date:        20220804
# URL: https://www.acmicpc.net/problem/3653

import sys

def update(arr, idx, val, n, l, r):
    if idx <= l and r <= idx:
        arr[n] = val
        return
    elif idx < l or r < idx:
        return
    m = (l + r) // 2
    update(arr, idx, val, 2 * n, l, m)
    update(arr, idx, val, 2 * n + 1, m + 1, r)
    arr[n] = arr[2 * n] + arr[2 * n + 1]
    return

def get_val(arr, ql, qr, n, l, r):
    if ql <= l and r <= qr:
        return arr[n]
    elif qr < l or r < ql:
        return 0
    m = (l + r) // 2
    l_val = get_val(arr, ql, qr, 2 * n, l, m)
    r_val = get_val(arr, ql, qr, 2 * n + 1, m + 1, r)
    return l_val + r_val

def main():
    t = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        queue = list(map(int, sys.stdin.readline().split()))
        arr = [0 for _ in range(4 * (n + m) + 10)]
        for i in range(n):
            update(arr, i + 1, 1, 1, 1, n + m)
        max_pos = n
        pos = [n + 1 - i for i in range(n + 1)]
        for q in queue:
            ans = get_val(arr, pos[q], max_pos, 1, 1, n + m) - 1
            print(ans, end=' ')
            update(arr, pos[q], 0, 1, 1, n + m)
            max_pos += 1
            pos[q] = max_pos
            update(arr, pos[q], 1, 1, 1, n + m)
        print()
    return

if __name__ == "__main__":
    main()