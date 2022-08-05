# Problem No.: 13323
# Solver:      Jinmin Goh
# Date:        20220805
# URL: https://www.acmicpc.net/problem/13323

import sys, heapq

def main():
    n = int(sys.stdin.readline().rstrip())
    nums = list(map(int, sys.stdin.readline().split()))
    queue = []
    ans = 0
    diff = 0
    heapq.heappush(queue, -nums[0])
    for i in range(1, n):
        end = -queue[0] + i
        if nums[i] <= end:
            ans += end - nums[i]
            heapq.heappop(queue)
            heapq.heappush(queue, -(nums[i] - i))
        heapq.heappush(queue, -(nums[i] - i))
    print(ans)
    return

if __name__ == "__main__":
    main()