# Problem No.: 10870
# Solver:      Jinmin Goh
# Date:        20220729
# URL: https://www.acmicpc.net/problem/10870

import sys

def main():
    n = int(input())
    f = [0, 1]
    for _ in range(n + 1):
        f.append(f[-1] + f[-2])
    print(f[n])
    return

if __name__ == "__main__":
    main()