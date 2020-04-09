# Problem No.: 11723
# Solver:      Jinmin Goh
# Date:        20200410
# URL: https://www.acmicpc.net/problem/11723

import sys

def main():
    n = int(input())
    numSet = set()
    for _ in range(n):
        order = list(sys.stdin.readline().split())
        if len(order) == 2:
            num = int(order[1])
        order = order[0]
        if order == "add":
            if num not in numSet:
                numSet.add(num)
        elif order == "check":
            if num in numSet:
                print(1)
            else:
                print(0)
        elif order == "remove":
            if num in numSet:
                numSet.remove(num)
        elif order == "toggle":
            if num in numSet:
                numSet.remove(num)
            else:
                numSet.add(num)
        elif order == "all":
            numSet = set([_ for _ in range(1, 21)])
        elif order == "empty":
            numSet = set()
    return

if __name__ == "__main__":
    main()