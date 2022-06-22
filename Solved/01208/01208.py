# Problem No.: 1208
# Solver:      Jinmin Goh
# Date:        20220622
# URL: https://www.acmicpc.net/problem/1208

import sys

def solve(nums, i, sum_val, res):
    if i == len(nums) - 1:
        res.append(sum_val)
        res.append(sum_val + nums[i])
    else:
        solve(nums, i + 1, sum_val, res)
        solve(nums, i + 1, sum_val + nums[i], res)

def main():
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    if n == 1:
        if s in nums:
            print(1)
        else:
            print(0)
        return
    res1 = []
    res2 = []
    solve(nums[:n // 2], 0, 0, res1)
    solve(nums[n // 2:], 0, 0, res2)
    d1 = {}
    d2 = {}
    for i in res1:
        if i not in d1:
            d1[i] = 0
        d1[i] += 1
    for i in res2:
        if i not in d2:
            d2[i] = 0
        d2[i] += 1
    ans = 0
    for i in d1:
        if s - i in d2:
            ans += d1[i] * d2[s - i]
    if s == 0:
        ans -= 1
    print(ans)
    return

if __name__ == "__main__":
    main()