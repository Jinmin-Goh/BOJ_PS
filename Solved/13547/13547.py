# Problem No.: 13547
# Solver:      Jinmin Goh
# Date:        20220812
# URL: https://www.acmicpc.net/problem/13547

import sys, math

def check(nums, cnt, idx, add, curr):
    if add:
        if cnt[nums[idx]] == 0:
            curr += 1
        cnt[nums[idx]] += 1
    else:
        cnt[nums[idx]] -= 1
        if cnt[nums[idx]] == 0:
            curr -= 1
    return curr

def main():
    n = int(sys.stdin.readline().rstrip())
    nums = list(map(int, sys.stdin.readline().split()))
    q = int(sys.stdin.readline().rstrip())
    query = []
    for i in range(q):
        a, b = map(int, sys.stdin.readline().split())
        query.append((a - 1, b - 1, i))
    rt = math.isqrt(n)
    query.sort(key=lambda x:(x[1] // rt, x[0]))
    l, r, curr = 1, 0, 0
    cnt = [0 for _ in range(1000001)]
    ans = [0 for _ in range(q + 1)]
    for i in range(q):
        while query[i][0] < l:
            l -= 1
            curr = check(nums, cnt, l, True, curr)
        while query[i][0] > l:
            curr = check(nums, cnt, l, False, curr)
            l += 1
        while query[i][1] < r:
            curr = check(nums, cnt, r, False, curr)
            r -= 1
        while query[i][1] > r:
            r += 1
            curr = check(nums, cnt, r, True, curr)
        ans[query[i][2]] = curr
    for i in range(q):
        print(ans[i])
    return

if __name__ == "__main__":
    main()