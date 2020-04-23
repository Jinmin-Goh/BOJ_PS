# Problem No.: 15663
# Solver:      Jinmin Goh
# Date:        20200423
# URL: https://www.acmicpc.net/problem/15663

import sys

def answer(nums: [int], n: int, m: int) -> None:
    ansSet = set()
    def backtrack(x: int, ans: [int]) -> None:
        if len(ans) == m:
            temp = []
            for i in ans:
                temp.append(nums[i])
            temp = tuple(temp)
            if temp in ansSet:
                return
            ansSet.add(temp)
            for i in temp:
                print(i, end = " ")
            print("")
            return
        for i in range(0, n):
            if i in ans:
                continue
            ans.append(i)
            backtrack(i, ans)
            ans.pop()

    for i in range(n):
        backtrack(i, [i])

def main():
    n, m = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    answer(nums, n, m)
    return

if __name__ == "__main__":
    main()