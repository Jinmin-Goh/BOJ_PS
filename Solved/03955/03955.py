# Problem No.: 3955
# Solver:      Jinmin Goh
# Date:        20200611
# URL: https://www.acmicpc.net/problem/3955

import sys
import math

# expanded euclidean algorithm

def expGCD(a: int, b: int) -> (int,):
    if b == 0:
        return (a, 1, 0)
    temp = expGCD(b, a % b)
    #print(a, b, temp)
    x, y = temp[1], temp[2]
    return (temp[0], y, x - (y * (a // b)))

# find solution of kx + 1 = cy, (k, c, x, y are all positive int)
# -kx + cy = 1 or kx + cy = 1 when x is negative int

def main():
    t = int(input())
    for _ in range(t):
        k, c = map(int, sys.stdin.readline().split())
        
        # exception for c = 1 case
        if c == 1:
            if k + 1 > 10 ** 9:
                print("IMPOSSIBLE")
            else:
                print(k + 1)
            continue
        
        ans = expGCD(k, c)

        # if gcd(k, c) != 1
        if ans[0] != 1:
            print("IMPOSSIBLE")
            continue
        # general solution: x = x0 + c * t / y = y0 - k * t
        # 0 > x and y > 0; x0 + c * t < 0 and y0 - k * t > 0
        # t < min(-x0 / c, y0 / k)
        # y <= 10 ** 9, k * t >= y0 - 10 ** 9
        x0 = ans[1]
        y0 = ans[2]
        maxVal = math.floor(min(-(x0 / c), y0 / k))
        minVal = y0 - 10 ** 9
        if minVal > (maxVal * k):
            print("IMPOSSIBLE")
        else:
            print(y0 - k * maxVal)
    return

if __name__ == "__main__":
    main()