# Problem No.: 2798
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/2798

import sys

def main():
    temp = input().split()
    n = int(temp[0])
    m = int(temp[1])
    nums = input().split()
    nums = [int(_) for _ in nums]
    ans = 0
    for i in range(n - 2):
        sumVal = nums[i]
        if sumVal > m:
            continue
        for j in range(i + 1, n - 1):
            sumVal2 = sumVal + nums[j]
            if sumVal2 > m:
                continue
            for k in range(j + 1, n):
                sumVal3 = sumVal2 + nums[k]
                if sumVal3 > m:
                    continue
                elif sumVal3 == m:
                    print(m)
                    return
                else:
                    ans = max(ans, sumVal3)
    print(ans)
    return

if __name__ == "__main__":
    main()