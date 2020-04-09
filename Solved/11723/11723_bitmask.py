# Problem No.: 11723
# Solver:      Jinmin Goh
# Date:        20200410
# URL: https://www.acmicpc.net/problem/11723

import sys

def main():
    n = int(input())
    mask = 0
    for _ in range(n):
        order = list(sys.stdin.readline().split())
        temp = None
        if len(order) == 2:
            num = int(order[1])
            temp = 1 << (num - 1)
        order = order[0]
        if order == "add":
            mask |= temp
        elif order == "check":
            if mask & temp:
                print(1)
            else:
                print(0)
        elif order == "remove":
            if mask & temp:
                mask ^= temp
        elif order == "toggle":
            mask ^= temp
        elif order == "all":
            mask = 0xFFFFF
        elif order == "empty":
            mask = 0
    return

if __name__ == "__main__":
    main()