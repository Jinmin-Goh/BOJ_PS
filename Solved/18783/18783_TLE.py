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

    # this loop is O(n ^ 2); TLE    
    ansTable = [ans[:]]
    while True:
        ansTable.append([None] * n)
        for i in range(n):
            ansTable[-1][change[i] - 1] = ansTable[-2][i]
        cnt += 1
        if ansTable[-1] == ansTable[0] or cnt >= k:
            if ansTable[-1] == ansTable[0]:
                ansTable.pop()
            break
    if cnt >= k:
        for i in ansTable[-1]:
            print(i)
        return
    
    k %= cnt
    
    for i in ansTable[k]:
        print(i)
    
    return

if __name__ == "__main__":
    main()