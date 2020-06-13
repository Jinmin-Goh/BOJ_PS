# Problem No.: 11047
# Solver:      Jinmin Goh
# Date:        20200611
# URL: https://www.acmicpc.net/problem/11047

import sys

def main():
    n, k = map(int, input().split())
    coin = []
    for _ in range(n):
        temp = int(sys.stdin.readline().strip())
        if temp > k:
            continue
        coin.append(temp)
    ans = 0
    for i in range(len(coin)):
        ans += k // coin[-i - 1]
        k = k % coin[-i - 1]
    print(ans)

    return

if __name__ == "__main__":
    main()