# Problem No.: 15666
# Solver:      Jinmin Goh
# Date:        20200423
# URL: https://www.acmicpc.net/problem/15666

import sys

def answer(nums: [int], n: int, m: int) -> None:
    def backtrack(x: int, ans: [int]) -> None:
        if len(ans) == m:
            for i in ans:
                print(nums[i], end = " ")
            print("")
            return
        for i in range(x, n):
            ans.append(i)
            backtrack(i, ans)
            ans.pop()

    for i in range(n):
        backtrack(i, [i])

def main():
    n, m = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    nums = list(set(nums))
    nums.sort()
    answer(nums, len(nums), m)
    return

if __name__ == "__main__":
    main()