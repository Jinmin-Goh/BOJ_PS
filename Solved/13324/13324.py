# Problem No.: 13324
# Solver:      Jinmin Goh
# Date:        20220805
# URL: https://www.acmicpc.net/problem/13324

import sys, heapq

def main():
    n = int(sys.stdin.readline().rstrip())
    nums = list(map(int, sys.stdin.readline().split()))
    queue = []
    ans = []
    for i in range(n):
        heapq.heappush(queue, -(nums[i] - i))
        ans.append(-queue[0])
        heapq.heappop(queue)
        heapq.heappush(queue, -(nums[i] - i))
    for i in reversed(range(n - 1)):
        ans[i] = min(ans[i], ans[i + 1])
    for i in range(n):
        print(ans[i] + i)
    return

if __name__ == "__main__":
    main()