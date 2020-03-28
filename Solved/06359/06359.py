# Problem No.: 6359
# Solver:      Jinmin Goh
# Date:        20200328
# URL: https://www.acmicpc.net/problem/6359

import sys

def main():
    n = int(input())
    dpList = [False] * 101
    for i in range(1, 101):
        temp = i
        while temp <= 100:
            dpList[temp] = not dpList[temp]
            temp += i
    for _ in range(n):
        print(sum(dpList[:int(input()) + 1]))
    return

if __name__ == "__main__":
    main()