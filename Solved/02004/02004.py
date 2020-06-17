# Problem No.: 2004
# Solver:      Jinmin Goh
# Date:        20200617
# URL: https://www.acmicpc.net/problem/2004

import sys

def main():
    n, m = map(int, input().split())

    temp = 5
    nVal = 0
    while temp <= n:
        nVal += n // temp
        temp *= 5
    
    temp = 5
    mVal = 0
    while temp <= m:
        mVal += m // temp
        temp *= 5
    diff = n - m
    temp = 5
    diffVal = 0
    while temp <= diff:
        diffVal += diff // temp
        temp *= 5
    
    val5 = nVal - mVal - diffVal 

    temp = 2
    nVal = 0
    while temp <= n:
        nVal += n // temp
        temp *= 2
    
    temp = 2
    mVal = 0
    while temp <= m:
        mVal += m // temp
        temp *= 2
    diff = n - m
    temp = 2
    diffVal = 0
    while temp <= diff:
        diffVal += diff // temp
        temp *= 2
    
    val2 = nVal - mVal - diffVal 

    print(min(val5, val2))

    return

if __name__ == "__main__":
    main()