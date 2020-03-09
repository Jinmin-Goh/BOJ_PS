# Problem No.: 1920
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/1920

import sys

def main():
    n = int(input())
    nList = map(int, input().split())
    nSet = set(nList)
    m = int(input())
    mList = map(int, input().split())
    for i in mList:
        if i in nSet:
            print(1)
        else:
            print(0)
    return

if __name__ == "__main__":
    main()