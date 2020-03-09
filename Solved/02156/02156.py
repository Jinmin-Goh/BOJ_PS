# Problem No.: 2156
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/2156

import sys

def main():
    n = int(input())
    val = []
    for i in range(n):
        val.append(int(input()))
    if n <= 2:
        print(sum(val))
        return
    if n == 3:
        print(sum(val) - min(val))
        return
    dpList = [0] * n
    dpList[0] = val[0]
    dpList[1] = sum(val[:2])
    dpList[2] = sum(val[:3]) - min(val[:3])
    for i in range(3, n):
        dpList[i] = max(val[i] + dpList[i - 2], val[i] + val[i - 1] + dpList[i - 3], dpList[i - 1])
    print(max(dpList))
    return

if __name__ == "__main__":
    main()