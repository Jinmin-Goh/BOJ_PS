# Problem No.: 1086
# Solver:      Jinmin Goh
# Date:        20220711
# URL: https://www.acmicpc.net/problem/1086

import sys

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    n = int(sys.stdin.readline().rstrip())
    nums = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    k = int(sys.stdin.readline())
    nums = [(nums[i] % k, 10 ** len(str(nums[i])) % k) for i in range(n)]
    dp_table = [[0 for _ in range(k)] for __ in range(1 << n)]
    for i in range(n):
        dp_table[1 << i][nums[i][0]] = 1
    for i in range(1 << n):
        for j in range(n):
            if i & (1 << j):
                continue
            for p in range(k):
                dp_table[i | (1 << j)][(p * nums[j][1] + nums[j][0]) % k] += dp_table[i][p]
    f = 1
    for i in range(n):
        f *= i + 1
    print(f"{dp_table[(1 << n) - 1][0] // gcd(f, dp_table[(1 << n) - 1][0])}/{f // gcd(f, dp_table[(1 << n) - 1][0])}")
    return

if __name__ == "__main__":
    main()