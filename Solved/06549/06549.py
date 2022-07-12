# Problem No.: 6549
# Solver:      Jinmin Goh
# Date:        20220712
# URL: https://www.acmicpc.net/problem/6549

import sys
sys.setrecursionlimit(100000)

arr = []
nums = []

def min_index(x, y):
    if x == -1:
        return y
    elif y == -1:
        return x
    elif nums[x - 1] == nums[y - 1]:
        return min(x, y)
    else:
        return x if nums[x - 1] < nums[y - 1] else y

def update(idx, n, l, r):
    if idx <= l and r <= idx:
        arr[n] = idx
        return
    elif idx < l or r < idx:
        return
    m = (l + r) // 2
    update(idx, 2 * n, l, m)
    update(idx, 2 * n + 1, m + 1, r)
    arr[n] = min_index(arr[2 * n], arr[2 * n + 1])
    return

def get_min(ql, qr, n, l, r):
    if ql <= l and r <= qr:
        return arr[n]
    elif qr < l or r < ql:
        return -1
    m = (l + r) // 2
    l_val = get_min(ql, qr, 2 * n, l, m)
    r_val = get_min(ql, qr, 2 * n + 1, m + 1, r)
    return min_index(l_val, r_val)

def solve(s, e, n):
    idx = get_min(s, e, 1, 1, n)
    area = (e - s + 1) * nums[idx - 1]
    if s <= idx - 1:
        area = max(area, solve(s, idx - 1, n))
    if idx + 1 <= e:
        area = max(area, solve(idx + 1, e, n))
    return area

def main():
    global arr, nums
    temp = sys.stdin.readline().rstrip()
    while temp != '0':
        nums = list(map(int, temp.split()))
        nums = nums[1:]
        n = len(nums)
        arr = [0 for _ in range(4 * n + 1)]
        for i in range(n):
            update(i + 1, 1, 1, n)
        ans = solve(1, n, n)
        print(ans)
        temp = sys.stdin.readline().rstrip()
    return

if __name__ == "__main__":
    main()