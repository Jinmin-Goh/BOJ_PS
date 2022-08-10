# Problem No.: 22193
# Solver:      Jinmin Goh
# Date:        20220810
# URL: https://www.acmicpc.net/problem/22193

import sys

def main():
    _, _ = map(int, sys.stdin.readline().split())
    a = int(sys.stdin.readline().rstrip())
    b = int(sys.stdin.readline().rstrip())
    print(a * b)
    return

if __name__ == "__main__":
    main()