# Problem No.: 9466
# Solver:      Jinmin Goh
# Date:        20220623
# URL: https://www.acmicpc.net/problem/9466

import sys
sys.setrecursionlimit(10 ** 6)

def solve(nums, visited, stack):
    if visited[stack[-1]] == 1:
        temp = stack.pop()
        visited[temp] = 2
        cnt = 1
        while stack[-1] != temp:
            visited[stack.pop()] = 2
            cnt += 1
        while stack:
            visited[stack.pop()] = 2
        return cnt
    elif visited[stack[-1]] == 2:
        while stack:
            visited[stack.pop()] = 2
        return 0
    else:
        visited[stack[-1]] = 1
        stack.append(nums[stack[-1]])
        return solve(nums, visited, stack)

def main():
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline())
        nums = list(map(int, sys.stdin.readline().split()))
        nums = [0] + nums
        ans = n
        # DFS
        visited = [0 for __ in range(n + 1)]    # 0: not visited; 1: in stack; 2: visited
        for i in range(1, n + 1):
            if visited[i] == 2:
                continue
            stack = [i]
            ans -= solve(nums, visited, stack)
        print(ans)

    return

if __name__ == "__main__":
    main()