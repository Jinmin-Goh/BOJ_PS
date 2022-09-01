# Problem No.: 16877
# Solver:      Jinmin Goh
# Date:        20220901
# URL: https://www.acmicpc.net/problem/16877

import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    nums = list(map(int, sys.stdin.readline().split()))
    f = [1 for _ in range(50)]
    f[1] = 2
    for i in range(2, 50):
        f[i] = f[i - 1] + f[i - 2]
    dp = [0 for _ in range(3 * 10 ** 6 + 1)]
    for i in range(1, 3 * (10 ** 6) + 1):
        visited = [False for _ in range(50)]
        j = 0
        while j < 50 and i - f[j] >= 0:
            visited[dp[i - f[j]]] = True
            j += 1
        for j in range(50):
            if visited[j] == False:
                dp[i] = j
                break
    ans = 0
    for i in nums:
        ans ^= dp[i]
    print('koosaga' if ans != 0 else 'cubelover')
    return

if __name__ == "__main__":
    main()