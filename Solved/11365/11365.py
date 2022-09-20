# Problem No.: 11365
# Solver:      Jinmin Goh
# Date:        20220920
# URL: https://www.acmicpc.net/problem/11365

import sys

def main():
    s = sys.stdin.readline().rstrip()
    while s != "END":
        s = ''.join(list(reversed(list(s))))
        print(s)
        s = sys.stdin.readline().rstrip()
    return

if __name__ == "__main__":
    main()