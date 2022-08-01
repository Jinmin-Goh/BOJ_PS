# Problem No.: 13171
# Solver:      Jinmin Goh
# Date:        20220801
# URL: https://www.acmicpc.net/problem/13171

import sys

def main():
    a = int(sys.stdin.readline().rstrip())
    x = int(sys.stdin.readline().rstrip())
    print(pow(a, x, 1000000007))

    return

if __name__ == "__main__":
    main()