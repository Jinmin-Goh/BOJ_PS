# Problem No.: 13548
# Solver:      Jinmin Goh
# Date:        20220812
# URL: https://www.acmicpc.net/problem/13548

import sys, math

def check(nums, cnt, cnt2, idx, add, curr):
    if add:
        cnt2[cnt[nums[idx]]] -= 1
        cnt[nums[idx]] += 1
        cnt2[cnt[nums[idx]]] += 1
        curr = max(curr, cnt[nums[idx]])
    else:
        cnt2[cnt[nums[idx]]] -= 1
        cnt[nums[idx]] -= 1
        cnt2[cnt[nums[idx]]] += 1
    return curr

def main():
    n = int(sys.stdin.readline().rstrip())
    nums = list(map(int, sys.stdin.readline().split()))
    nums = [0] + nums
    q = int(sys.stdin.readline().rstrip())
    query = []
    for i in range(q):
        a, b = map(int, sys.stdin.readline().split())
        query.append((a, b, i))
    rt = math.isqrt(n)
    query.sort(key=lambda x:(x[1] // rt, x[0]))
    l, r, curr = 1, 0, 0
    cnt = [0 for _ in range(100001)]
    cnt2 = [0 for _ in range(100001)]
    cnt2[0] = n
    ans = [0 for _ in range(q)]
    for i in range(q):
        while query[i][0] < l:
            l -= 1
            curr = check(nums, cnt, cnt2, l, True, curr)
        while query[i][0] > l:
            curr = check(nums, cnt, cnt2, l, False, curr)
            l += 1
        while query[i][1] < r:
            curr = check(nums, cnt, cnt2, r, False, curr)
            r -= 1
        while query[i][1] > r:
            r += 1
            curr = check(nums, cnt, cnt2, r, True, curr)
        while cnt2[curr] == 0:
            curr -= 1
        ans[query[i][2]] = curr
    for i in range(q):
        print(ans[i])
    return

if __name__ == "__main__":
    main()