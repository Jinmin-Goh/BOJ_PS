# Problem No.: 3733
# Solver:      Jinmin Goh
# Date:        20220910
# URL: https://www.acmicpc.net/problem/3733

import sys

def main():
    temp = sys.stdin.readline().rstrip()
    while temp:
        a, b = map(int, temp.split())
        print(b // (a + 1))
        temp = sys.stdin.readline().rstrip()
    return

if __name__ == "__main__":
    main()