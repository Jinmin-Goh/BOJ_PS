# Problem No.: 2292
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/2292

import sys

def main():
    n = int(input())
    if n == 1:
        print(1)
        return
    sum = 1
    i = 1
    while True:
        sum += i * 6
        if sum >= n:
            print(i + 1)
            return
        i += 1
    return

if __name__ == "__main__":
    main()