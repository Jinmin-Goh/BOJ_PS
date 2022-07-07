# Problem No.: 14428
# Solver:      Jinmin Goh
# Date:        20220707
# URL: https://www.acmicpc.net/problem/14428

import sys

sys.setrecursionlimit(200000)

def min_index(nums, x, y):
    if x == -1:
        return y
    elif y == -1:
        return x
    elif nums[x - 1] == nums[y - 1]:
        return min(x, y)
    else:
        return x if nums[x - 1] < nums[y - 1] else y

def update(nums, arr, idx, n, l, r):
    if idx <= l and r <= idx:
        arr[n] = idx
        return
    elif idx < l or r < idx:
        return
    m = (l + r) // 2
    update(nums, arr, idx, 2 * n, l, m)
    update(nums, arr, idx, 2 * n + 1, m + 1, r)
    arr[n] = min_index(nums, arr[2 * n], arr[2 * n + 1])
    return

def print_min(nums, arr, ql, qr, n, l, r):
    if ql <= l and r <= qr:
        return arr[n]
    elif qr < l or r < ql:
        return -1
    m = (l + r) // 2
    l_val = print_min(nums, arr, ql, qr, 2 * n, l, m)
    r_val = print_min(nums, arr, ql, qr, 2 * n + 1, m + 1, r)
    return min_index(nums, l_val, r_val)
    
def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    m = int(input())
    arr = [0 for _ in range(4 * n + 1)]
    for i in range(n):
        update(nums, arr, i + 1, 1, 1, n)
    for _ in range(m):
        q, a, b = map(int, sys.stdin.readline().split())
        if q == 1:
            nums[a - 1] = b
            update(nums, arr, a, 1, 1, n)
        elif q == 2:
            print(print_min(nums, arr, a, b, 1, 1, n))
    return

if __name__ == "__main__":
    main()