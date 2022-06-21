# Problem No.: 14225
# Solver:      Jinmin Goh
# Date:        20220621
# URL: https://www.acmicpc.net/problem/14225

import sys

def solve(nums, i, sum_val, res):
    if i == len(nums) - 1:
        res.append(sum_val)
        res.append(sum_val + nums[i])
    else:
        solve(nums, i + 1, sum_val, res)
        solve(nums, i + 1, sum_val + nums[i], res)

def main():
    n = map(int, input())
    nums = list(map(int, input().split()))
    nums.sort()
    res = []
    solve(nums, 0, 0, res)
    res = set(res)
    ans = 1
    while True:
        if ans in res:
            ans += 1
        else:
            break
    print(ans)
    return

if __name__ == "__main__":
    main()