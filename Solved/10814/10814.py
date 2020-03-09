# Problem No.: 10814
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/10814

import sys

def main():
    n = int(input())
    data = []
    for i in range(n):
        temp = input().split()
        data.append((int(temp[0]), i, temp[1]))
    data.sort()
    for i in data:
        print(i[0],i[2])
    return

if __name__ == "__main__":
    main()