# Problem No.: 11720
# Solver:      Jinmin Goh
# Date:        20200308
# URL: https://www.acmicpc.net/problem/11720

import sys

def main():
    n = int(input())
    num = input()
    sum = 0
    for i in num:
        sum += int(i)
    print(sum)
    return

if __name__ == "__main__":
    main()