# Problem No.: 01806
# Solver:      Jinmin Goh
# Date:        20220614
# URL: https://www.acmicpc.net/problem/01806

import sys

def main():
    n, s = map(int, input().split())
    nums = list(input().split())
    for i in range(n):
        nums[i] = int(nums[i])
    
    p1 = 0
    p2 = 0
    ans = n + 1
    sumVal = nums[0]
    while p1 < n and p2 < n:
        if sumVal >= s:
            ans = min(ans, p2 - p1 + 1)
            p1 += 1
            sumVal -= nums[p1 - 1]
        else:
            p2 += 1
            if p2 >= n:
                break
            sumVal += nums[p2]

    if ans != n + 1:
        print(ans)
    else:
        print(0)

    return

if __name__ == "__main__":
    main()