# Problem No.: 2180
# Solver:      Jinmin Goh
# Date:        20220617
# URL: https://www.acmicpc.net/problem/2180

import sys
from functools import cmp_to_key

def cmp(x, y):
    (a1, b1) = x
    (a2, b2) = y
    return (b1 * (a2 - 1)) - (b2 * (a1 - 1))

def main():
    n = int(sys.stdin.readline())
    time = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        time.append((a + 1, b))
    # consider (a_i, b_i) and (a_j, b_j) where i < j
    # if time is x, then a_j * (a_i * x + b_i) + b_j <= a_i * (a_j * x + b_j) + b_i
    # which means, (a_j - 1) * b_i <= (a_i - 1) * b_j
    time.sort(reverse=True)
    pos = n
    for i in range(n):
        (a, b) = time[i]
        if a <= 1:
            pos = i
            break
    ratio = time[:pos]
    ratio.sort(key=cmp_to_key(cmp))
    ans = 0
    for (a, b) in ratio:
        ans = a * ans + b
        ans %= 40000
    for i in range(pos, n):
        (a, b) = time[i]
        ans = a * ans + b
        ans %= 40000
    print(ans)
    
    return

if __name__ == "__main__":
    main()