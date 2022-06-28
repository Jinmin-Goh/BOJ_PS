# Problem No.: 1007
# Solver:      Jinmin Goh
# Date:        20220628
# URL: https://www.acmicpc.net/problem/1007

import sys
from itertools import combinations

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        x_sum = 0
        y_sum = 0
        dots = []
        for __ in range(n):
            a, b = map(int, sys.stdin.readline().split())
            x_sum += a
            y_sum += b
            dots.append((a, b))
        comb = list(combinations(dots, n // 2))
        min_val = 10 ** 9
        for temp in comb:
            temp_x_sum = 0
            temp_y_sum = 0
            for dot in temp:
                temp_x_sum += dot[0]
                temp_y_sum += dot[1]
            temp_x_sum = x_sum - 2 * temp_x_sum
            temp_y_sum = y_sum - 2 * temp_y_sum
            min_val = min(min_val, (temp_x_sum ** 2 + temp_y_sum ** 2) ** 0.5)
        print(min_val)
    return

if __name__ == "__main__":
    main()