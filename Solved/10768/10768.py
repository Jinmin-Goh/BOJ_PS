# Problem No.: 10768
# Solver:      Jinmin Goh
# Date:        20220915
# URL: https://www.acmicpc.net/problem/10768

import sys

def main():
    a = int(sys.stdin.readline().rstrip())
    b = int(sys.stdin.readline().rstrip())
    if a < 2:
        print("Before")
    elif a == 2:
        if b < 18:
            print("Before")
        elif b == 18:
            print("Special")
        else:
            print("After")
    else:
        print("After")
    return

if __name__ == "__main__":
    main()