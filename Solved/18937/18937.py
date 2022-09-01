# Problem No.: 18937
# Solver:      Jinmin Goh
# Date:        20220901
# URL: https://www.acmicpc.net/problem/18937

import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    nums = list(map(int, sys.stdin.readline().split()))
    king = sys.stdin.readline().rstrip()
    ans = 0
    for i in nums:
        ans ^= i - 2
    if ans:
        if king == "Whiteking":
            print("Whiteking")
        else:
            print("Blackking")
    else:
        if king == "Whiteking":
            print("Blackking")
        else:
            print("Whiteking")

    return

if __name__ == "__main__":
    main()