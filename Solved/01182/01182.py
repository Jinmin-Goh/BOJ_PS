# Problem No.: 1182
# Solver:      Jinmin Goh
# Date:        20220621
# URL: https://www.acmicpc.net/problem/1182

import sys

def solve(nums, s, i, sum_val, cnt):
    if i == len(nums) - 1:
        ans = 0
        if sum_val + nums[i] == s:
            ans +=  1
        if sum_val == s and cnt:
            ans += 1
        return ans
    else:
        return solve(nums, s, i + 1, sum_val, cnt) + solve(nums, s, i + 1, sum_val + nums[i], cnt + 1)

def main():
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    ans = solve(nums, s, 0, 0, 0)
    print(ans)
    return

if __name__ == "__main__":
    main()