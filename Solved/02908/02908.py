# Problem No.: 2908
# Solver:      Jinmin Goh
# Date:        20200308
# URL: https://www.acmicpc.net/problem/2908

import sys

def main():
    n = input().split()
    rev = []
    temp = ""
    for i in n[0]:
        temp = i + temp
    rev.append(int(temp))
    temp = ""
    for i in n[1]:
        temp = i + temp
    rev.append(int(temp))
    print(max(rev))
    return

if __name__ == "__main__":
    main()