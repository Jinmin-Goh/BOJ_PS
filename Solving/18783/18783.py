# Problem No.: 18783
# Solver:      Jinmin Goh
# Date:        20200713
# URL: https://www.acmicpc.net/problem/18783

import sys

def main():
    n, m, k = map(int, input().split())
    nums = []
    for _ in range(m):
        nums.append(list(map(int, sys.stdin.readline().split())))
    
    ref = [_ + 1 for _ in range(n)]
    change = [_ + 1 for _ in range(n)]
    ans = [_ + 1 for _ in range(n)]
    
    # find final change result for single process
    cnt = 0
    for i in range(m):
        temp = list(reversed(change[nums[i][0] - 1:nums[i][1]]))
        change[nums[i][0] - 1:nums[i][1]] = temp

    while True:
        temp = [None] * n
        for i in range(n):
            temp[change[i] - 1] = ans[i]
        ans = temp[:]
        #print(ans)
        cnt += 1
        if ans == ref:
            break
    
    ans = [_ + 1 for _ in range(n)]
    k %= cnt
    for _ in range(k):
        temp = [None] * n
        for i in range(n):
            temp[change[i] - 1] = ans[i]
        ans = temp[:]
        #print(ans)
    
    for i in ans:
        print(i)
    
    return

if __name__ == "__main__":
    main()