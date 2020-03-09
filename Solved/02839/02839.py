# Problem No.: 2839
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/2839

import sys

def main():
    n = int(input())
    if n == 4 or n == 7:
        print(-1)
        return
    temp = 0
    if n > 12:
        temp = (n - 8) // 5
        n -= 5 * temp
    if n == 3 or n == 5:
        print(1 + temp)
        return
    if n == 6 or n == 8 or n == 10:
        print(2 + temp)
        return
    if n == 9 or n == 11:
        print(3 + temp)
        return
    if n == 12:
        print(4 + temp)
    return

if __name__ == "__main__":
    main()