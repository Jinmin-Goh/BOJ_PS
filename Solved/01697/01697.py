# Problem No.: 1697
# Solver:      Jinmin Goh
# Date:        20200606
# URL: https://www.acmicpc.net/problem/1697

import sys
import collections

def main():
    n, k = map(int, input().split())
    if n > k:
        print(n - k)
        return
    ans = [0] * (100001)
    deq = collections.deque([n])
    while True:
        #print(deq)
        while True:
            val = deq.popleft()
            if val == k:
                print(ans[val])
                return
            if val - 1 >= 0 and not ans[val - 1]:
                deq.append(val - 1)
                ans[val - 1] = ans[val] + 1
            if val + 1 <= 100000 and not ans[val + 1]:
                deq.append(val + 1)
                ans[val + 1] = ans[val] + 1
            if val * 2 <= 100000 and not ans[val * 2]:
                deq.append(val * 2)
                ans[val * 2] = ans[val] + 1
            
            #print(deq)
        ans += 1

    return

if __name__ == "__main__":
    main()