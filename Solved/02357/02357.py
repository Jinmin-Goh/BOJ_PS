# Problem No.: 2357
# Solver:      Jinmin Goh
# Date:        20220707
# URL: https://www.acmicpc.net/problem/2357

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

def max_index(nums, x, y):
    if x == -1:
        return y
    elif y == -1:
        return x
    elif nums[x - 1] == nums[y - 1]:
        return max(x, y)
    else:
        return x if nums[x - 1] > nums[y - 1] else y

def update(nums, min_arr, max_arr, idx, n, l, r):
    if idx <= l and r <= idx:
        min_arr[n] = idx
        max_arr[n] = idx
        return
    elif idx < l or r < idx:
        return
    m = (l + r) // 2
    update(nums, min_arr, max_arr, idx, 2 * n, l, m)
    update(nums, min_arr, max_arr, idx, 2 * n + 1, m + 1, r)
    min_arr[n] = min_index(nums, min_arr[2 * n], min_arr[2 * n + 1])
    max_arr[n] = max_index(nums, max_arr[2 * n], max_arr[2 * n + 1])
    return

def print_min(nums, min_arr, max_arr, ql, qr, n, l, r):
    if ql <= l and r <= qr:
        return (min_arr[n], max_arr[n])
    elif qr < l or r < ql:
        return (-1, -1)
    m = (l + r) // 2
    l_min_val, l_max_val = print_min(nums, min_arr, max_arr, ql, qr, 2 * n, l, m)
    r_min_val, r_max_val = print_min(nums, min_arr, max_arr, ql, qr, 2 * n + 1, m + 1, r)
    return (min_index(nums, l_min_val, r_min_val), max_index(nums, l_max_val, r_max_val))
    
def main():
    n, m = map(int, input().split())
    nums = [int(sys.stdin.readline()) for _ in range(n)]
    min_arr = [0 for _ in range(4 * n + 1)]
    max_arr = [0 for _ in range(4 * n + 1)]
    for i in range(n):
        update(nums, min_arr, max_arr, i + 1, 1, 1, n)
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        val = print_min(nums, min_arr, max_arr, a, b, 1, 1, n)
        print(nums[val[0] - 1], nums[val[1] - 1])
    return

if __name__ == "__main__":
    main()