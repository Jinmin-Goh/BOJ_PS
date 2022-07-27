# Problem No.: 2754
# Solver:      Jinmin Goh
# Date:        20220727
# URL: https://www.acmicpc.net/problem/2754

import sys

def main():
    n = input()
    d = {'-':-0.3, '0':0, '+':0.3}
    print(0.0 if n == 'F' else float(69 - ord(n[0])) + d[n[1]])
    return

if __name__ == "__main__":
    main()