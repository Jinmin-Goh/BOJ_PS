# Problem No.: 11871
# Solver:      Jinmin Goh
# Date:        20220901
# URL: https://www.acmicpc.net/problem/11871

import sys

def main():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    ans = 0
    for i in nums:
        if i % 2:
            ans ^= (i + 1) // 2
        else:
            ans ^= (i - 1) // 2
    print('koosaga' if ans != 0 else 'cubelover')
    return

if __name__ == "__main__":
    main()