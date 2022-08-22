# Problem No.: 16978
# Solver:      Jinmin Goh
# Date:        20220822
# URL: https://www.acmicpc.net/problem/16978

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

def get_sum(arr, ql, qr, n, l, r):
    if ql <= l and r <= qr:
        return arr[n]
    elif qr < l or r < ql:
        return 0
    m = (l + r) // 2
    l_val = get_sum(arr, ql, qr, 2 * n, l, m)
    r_val = get_sum(arr, ql, qr, 2 * n + 1, m + 1, r)
    return l_val + r_val

def main():
    n = int(sys.stdin.readline().rstrip())
    nums = list(map(int, sys.stdin.readline().split()))
    q = int(sys.stdin.readline().rstrip())
    query_1 = []
    query_2 = []
    cnt = 0
    for _ in range(q):
        query = list(map(int, sys.stdin.readline().split()))
        if query[0] == 1:
            query_1.append(tuple(query))
        else:
            query.append(cnt)
            cnt += 1
            query_2.append(tuple(query))
    query_2.sort()
    arr = [0 for _ in range(400010)]
    for i in range(n):
        update(arr, i + 1, nums[i], 1, 1, n)
    ans = [0 for _ in range(cnt)]
    cnt = 0
    for _, k, i, j, pos in query_2:
        while cnt < k:
            _, p, v = query_1[cnt]
            update(arr, p, v, 1, 1, n)
            cnt += 1
        ans[pos] = get_sum(arr, i, j, 1, 1, n)
    for i in ans:
        print(i)

    return

if __name__ == "__main__":
    main()