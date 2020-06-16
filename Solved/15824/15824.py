# Problem No.: 15824
# Solver:      Jinmin Goh
# Date:        20200616
# URL: https://www.acmicpc.net/problem/15824

import sys

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    data = [1]
    for i in range(n - 1):
        data.append((data[-1] * 2) % 1000000007)
    nums.sort()
    ans = 0
    for i in range(n):
        ans += (nums[i] * (data[i] - data[n - 1 - i])) % 1000000007
    print(ans % 1000000007)
    return

if __name__ == "__main__":
    main()