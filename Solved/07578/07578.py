# Problem No.: 7578
# Solver:      Jinmin Goh
# Date:        20220712
# URL: https://www.acmicpc.net/problem/7578

import sys

arr = [0 for _ in range(4 * 500000 + 1)]

def update(idx, val, n, l, r):
    if idx <= l and r <= idx:
        arr[n] = val
        return
    elif idx < l or r < idx:
        return
    m = (l + r) // 2
    update(idx, val, 2 * n, l, m)
    update(idx, val, 2 * n + 1, m + 1, r)
    arr[n] = arr[2 * n] + arr[2 * n + 1]
    return

def get_val(ql, qr, n, l, r):
    if ql <= l and r <= qr:
        return arr[n]
    elif qr < l or r < ql:
        return 0
    m = (l + r) // 2
    l_val = get_val(ql, qr, 2 * n, l, m)
    r_val = get_val(ql, qr, 2 * n + 1, m + 1, r)
    return l_val + r_val

def main():
    n = int(sys.stdin.readline().rstrip())
    upper = list(map(int, sys.stdin.readline().split()))
    mapping = {upper[i]:i + 1 for i in range(n)}
    lower = list(map(int, sys.stdin.readline().split()))
    lower = [mapping[lower[i]] for i in range(n)]
    ans = 0
    for i in range(n):
        ans += get_val(lower[i], n, 1, 1, n)
        update(lower[i], 1, 1, 1, n)
    print(ans)
    return

if __name__ == "__main__":
    main()