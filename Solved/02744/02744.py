# Problem No.: 2744
# Solver:      Jinmin Goh
# Date:        20220726
# URL: https://www.acmicpc.net/problem/2744

import sys

def main():
    s = sys.stdin.readline().rstrip()
    ans = []
    for i in s:
        if ord(i) < 91:
            ans.append(chr(ord(i) + 32))
        else:
            ans.append(chr(ord(i) - 32))
    print(''.join(ans))
    return

if __name__ == "__main__":
    main()