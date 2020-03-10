# Problem No.: 1912
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/1912

import sys

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    if n == 1:
        print(nums[0])
        return
    numSum = [0] * (n + 1)
    maxVal = -(2 ** 31)
    for i in range(n):
        numSum[i + 1] = max(numSum[i] + nums[i], nums[i])
        maxVal = max(maxVal, numSum[i + 1])
    print(maxVal)
    return

if __name__ == "__main__":
    main()