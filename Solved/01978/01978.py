# Problem No.: 1978
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/1978

import sys

def main():
    n = int(input())
    nums = map(int, input().split())
    pCheckList = [True] * 1001
    pCheckList[0] = False
    pCheckList[1] = False
    for i in range(2, int(1001 ** 0.5) + 1):
        if pCheckList[i]:
            cnt = i * 2
            while cnt < 1001:
                pCheckList[cnt] = False
                cnt += i
    pSet = set()
    for i in range(1001):
        if pCheckList[i]:
            pSet.add(i)
    ans = 0
    for i in nums:
        if i in pSet:
            ans += 1
    print(ans)
    return

if __name__ == "__main__":
    main()