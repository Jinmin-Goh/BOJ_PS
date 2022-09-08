# Problem No.: 24309
# Solver:      Jinmin Goh
# Date:        20220908
# URL: https://www.acmicpc.net/problem/24309

import sys

def main():
    a = int(sys.stdin.readline().rstrip())
    b = int(sys.stdin.readline().rstrip())
    c = int(sys.stdin.readline().rstrip())
    print((b - c) // a)
    return

if __name__ == "__main__":
    main()