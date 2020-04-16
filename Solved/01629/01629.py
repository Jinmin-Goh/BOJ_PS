# Problem No.: 1629
# Solver:      Jinmin Goh
# Date:        20200415
# URL: https://www.acmicpc.net/problem/1629

import sys

def main():
    a, b, c = map(int, input().split())
    a = a % c
    ans = 1
    temp = a
    while b > 0:
        if b % 2:
            ans *= temp
            ans = ans % c
        temp = temp ** 2 % c
        b >>= 1
    print(ans)
    return

if __name__ == "__main__":
    main()