# Problem No.: 13335
# Solver:      Jinmin Goh
# Date:        20220913
# URL: https://www.acmicpc.net/problem/13335

import sys

def main():
    n, w, l = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    bridge = [0 for _ in range(w)]
    p = 0
    weight = 0
    ans = 0
    while p < n:
        if bridge[0] != 0:
            weight -= bridge[0]
            bridge[0] = 0
        for i in range(w - 1):
            bridge[i], bridge[i + 1] = bridge[i + 1], bridge[i]
        if weight + nums[p] <= l:
            bridge[-1] = nums[p]
            weight += nums[p]
            p += 1
        ans += 1
    ans += w
    print(ans)
    return

if __name__ == "__main__":
    main()