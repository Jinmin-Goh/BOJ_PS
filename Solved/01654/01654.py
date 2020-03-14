# Problem No.: 1654
# Solver:      Jinmin Goh
# Date:        20200314
# URL: https://www.acmicpc.net/problem/1654

import sys

def main():
    k, n = map(int, input().split())
    wire = []
    maxVal = 0
    for i in range(k):
        temp = int(sys.stdin.readline())
        wire.append(temp)
        maxVal = max(maxVal, temp)
    front = 1
    rear = maxVal
    ans = 0
    while 1 <= front <= rear <= maxVal:
        mid = (front + rear) // 2
        tempMidSum = 0
        for i in wire:
            tempMidSum += i // mid
        if tempMidSum >= n:
            front = mid + 1
            ans = max(mid, ans)
        else:
            rear = mid - 1
    print(ans)
    return

if __name__ == "__main__":
    main()