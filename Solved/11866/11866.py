# Problem No.: 11866
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/11866

import sys

def main():
    n, k = map(int, input().split())
    pos = k - 1
    nums = [i + 1 for i in range(n)]
    ans = []
    while nums:
        ans.append(nums.pop(pos))
        if not nums:
            break
        pos = (pos + k - 1) % len(nums)
    ansStr = "<"
    for i in ans:
        ansStr += str(i) + ", "
    ansStr = ansStr[:-2] + ">"
    print(ansStr)
    return

if __name__ == "__main__":
    main()