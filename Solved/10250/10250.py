# Problem No.: 10250
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/10250

import sys

def main():
    n = int(input())
    ans = []
    for i in range(n):
        temp = input().split()
        temp = [int(_) for _ in temp]
        if temp[2] % temp[0]:
            ans.append((temp[2] % temp[0]) * 100 + (temp[2] // temp[0]) + 1)
        else:
            ans.append(temp[0] * 100 + (temp[2] // temp[0]))
    for i in ans:
        print(i)
    return

if __name__ == "__main__":
    main()