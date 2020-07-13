# Problem No.: 18788
# Solver:      Jinmin Goh
# Date:        20200713
# URL: https://www.acmicpc.net/problem/18788

import sys

def main():
    n, k = map(int, input().split())
    a1, a2 = map(int, input().split())
    b1, b2 = map(int, input().split())

    ref = [_ + 1 for _ in range(n)]
    nums = [_ + 1 for _ in range(n)]
    cnt = 0

    while True:
        tempA = list(reversed(nums[a1 - 1:a2]))
        nums[a1 - 1:a2] = tempA
        tempB = list(reversed(nums[b1 - 1:b2]))
        nums[b1 - 1:b2] = tempB
        cnt += 1
        if nums == ref:
            break
    k %= cnt
    for i in range(k):
        tempA = list(reversed(nums[a1 - 1:a2]))
        nums[a1 - 1:a2] = tempA
        tempB = list(reversed(nums[b1 - 1:b2]))
        nums[b1 - 1:b2] = tempB
    
    for i in nums:
        print(i)



    return

if __name__ == "__main__":
    main()