# Problem No.: 18251
# Solver:      Jinmin Goh
# Date:        20220829
# URL: https://www.acmicpc.net/problem/18251

import sys

def dfs(depth, index, n, curr, d):
    if curr > n:
        return
    depth[curr] = d
    dfs(depth,index, n, 2 * curr, d + 1)
    index.append(curr)
    dfs(depth,index, n, 2 * curr + 1, d + 1)

def main():
    n = int(sys.stdin.readline().rstrip())
    nums = [0] + list(map(int, sys.stdin.readline().split()))
    depth = [0 for _ in range(n + 1)]
    index = []
    dfs(depth, index, n, 1, 0)
    ans = -10 ** 16
    for i in range(depth[n] + 1):
        for j in range(i, depth[n] + 1):
            temp = -10 ** 16
            for k in range(n):
                if depth[index[k]] < i or depth[index[k]] > j:
                    continue
                temp = max(temp + nums[index[k]], nums[index[k]])
                ans = max(ans, temp)
    print(ans)
    return

if __name__ == "__main__":
    main()