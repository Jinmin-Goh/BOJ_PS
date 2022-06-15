# Problem No.: 9527
# Solver:      Jinmin Goh
# Date:        20220615
# URL: https://www.acmicpc.net/problem/9527

import sys

def count(n):
    bitList = []
    while n:
        if n % 2:
            bitList.append(True)
        else:
            bitList.append(False)
        n >>= 1
    cnt = 0
    result = 0
    while bitList:
        bit = bitList.pop()
        if bit:
            result += (2 ** (len(bitList) - 1)) * len(bitList) + (2 ** len(bitList)) * cnt if bitList else cnt
            cnt += 1
    return result + cnt

def main():
    a, b = map(int, input().split())
    print(count(b) - count(a - 1))
    return

if __name__ == "__main__":
    main()