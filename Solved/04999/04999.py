# Problem No.: 4999
# Solver:      Jinmin Goh
# Date:        20220908
# URL: https://www.acmicpc.net/problem/4999

import sys

def main():
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()
    print("go" if len(a) >= len(b) else "no")
    return

if __name__ == "__main__":
    main()