# Problem No.: 2243
# Solver:      Jinmin Goh
# Date:        20220801
# URL: https://www.acmicpc.net/problem/2243

import sys

def update(arr, idx, val, n, l, r):
    if idx <= l and r <= idx:
        arr[n] += val
        return
    elif idx < l or r < idx:
        return
    m = (l + r) // 2
    update(arr, idx, val, 2 * n, l, m)
    update(arr, idx, val, 2 * n + 1, m + 1, r)
    arr[n] = arr[2 * n] + arr[2 * n + 1]

def get_val(arr, val, n, l, r):
    if l == r:
        return l
    m = (l + r) // 2
    if val <= arr[2 * n]:
        return get_val(arr, val, 2 * n, l, m)
    else:
        return get_val(arr, val - arr[2 * n], 2 * n + 1, m + 1, r)

def main():
    n = int(sys.stdin.readline().rstrip())
    arr = [0 for _ in range(4000001)]
    for _ in range(n):
        q = tuple(map(int, sys.stdin.readline().split()))
        if q[0] == 1:
            _, a = q
            ans = get_val(arr, a, 1, 1, 1000000)
            print(ans)
            update(arr, ans, -1, 1, 1, 1000000)
        else:
            _, a, b = q
            update(arr, a, b, 1, 1, 1000000)
    return

if __name__ == "__main__":
    main()