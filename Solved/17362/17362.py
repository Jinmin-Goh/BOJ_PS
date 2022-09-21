# Problem No.: 17362
# Solver:      Jinmin Goh
# Date:        20220921
# URL: https://www.acmicpc.net/problem/17362

import sys

def main():
    n = int(sys.stdin.readline().rstrip()) % 8
    dict = {1:1, 2:2, 3:3, 4:4, 5:5, 6:4, 7:3, 0:2}
    print(dict[n])
    return

if __name__ == "__main__":
    main()