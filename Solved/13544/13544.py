# Problem No.: 13544
# Solver:      Jinmin Goh
# Date:        20220824
# URL: https://www.acmicpc.net/problem/13544

import sys

def update(arr, idx, val, n, l, r):
    if idx <= l and r <= idx:
        arr[n].append(val)
        return
    elif idx < l or r < idx:
        return
    arr[n].append(val)
    m = (l + r) // 2
    update(arr, idx, val, 2 * n, l, m)
    update(arr, idx, val, 2 * n + 1, m + 1, r)
    return

def search(arr, ql, qr, val, n, l, r):
    if ql <= l and r <= qr:
        p1 = 0
        p2 = len(arr[n]) - 1
        while p1 < p2:
            m = (p1 + p2) // 2
            if arr[n][m] <= val:
                p1 = m + 1
            else:
                p2 = m
        if arr[n][p2] <= val:
            p2 += 1
        return len(arr[n]) - p2
    elif qr < l or r < ql:
        return 0
    m = (l + r) // 2
    l_val = search(arr, ql, qr, val, 2 * n, l, m)
    r_val = search(arr, ql, qr, val, 2 * n + 1, m + 1, r)
    return l_val + r_val

def main():
    n = int(sys.stdin.readline().rstrip())
    nums = list(map(int, sys.stdin.readline().split()))
    q = int(sys.stdin.readline().rstrip())
    arr = [[] for _ in range(400010)]
    for i in range(n):
        update(arr, i + 1, nums[i], 1, 1, n)
    for i in range(1, 400010):
        if not arr[i]:
            break
        arr[i].sort()
    ans = 0
    for _ in range(q):
        i, j, k = map(int, sys.stdin.readline().split())
        ans = search(arr, i ^ ans, j ^ ans, k ^ ans, 1, 1, n)
        print(ans)
    return

if __name__ == "__main__":
    main()