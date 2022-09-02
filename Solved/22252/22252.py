# Problem No.: 22252
# Solver:      Jinmin Goh
# Date:        20220902
# URL: https://www.acmicpc.net/problem/22252

import sys, heapq

def main():
    q = int(sys.stdin.readline().rstrip())
    pq_dict = {}
    ans = 0
    for _ in range(q):
        queue = list(map(str, sys.stdin.readline().split()))
        if queue[0] == '1':
            name = queue[1]
            nums = list(map(int, queue[3:]))
            if name not in pq_dict:
                pq_dict[name] = []
            for i in nums:
                heapq.heappush(pq_dict[name], -i)
        else:
            name = queue[1]
            cnt = int(queue[2])
            while name in pq_dict and pq_dict[name] and cnt > 0:
                ans += -heapq.heappop(pq_dict[name])
                cnt -= 1
    print(ans)
    return

if __name__ == "__main__":
    main()