# Problem No.: 9086
# Solver:      Jinmin Goh
# Date:        20220728
# URL: https://www.acmicpc.net/problem/9086

import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        s = sys.stdin.readline().rstrip()
        print(s[0] + s[-1])
    return

if __name__ == "__main__":
    main()