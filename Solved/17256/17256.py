# Problem No.: 17256
# Solver:      Jinmin Goh
# Date:        20220818
# URL: https://www.acmicpc.net/problem/17256

import sys

def main():
    a_x, a_y, a_z = map(int, sys.stdin.readline().split())
    c_x, c_y, c_z = map(int, sys.stdin.readline().split())
    print(c_x - a_z, c_y // a_y, c_z - a_x)
    return

if __name__ == "__main__":
    main()