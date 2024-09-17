# Problem No.: 30527
# Solver:      Jinmin Goh
# Date:        20240917
# URL: https://www.acmicpc.net/problem/30527

import sys

def main():
    nums = list(map(int, sys.stdin.readline().split()))
    n, k = map(int, sys.stdin.readline().split())
    sum_val = 0
    for i in range(5):
        sum_val += nums[2 * i] * nums[2 * i + 1]
    sum_val //= 5
    print(sum_val * n // k)

if __name__ == "__main__":
    main()