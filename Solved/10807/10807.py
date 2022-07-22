# Problem No.: 10807
# Solver:      Jinmin Goh
# Date:        20220722
# URL: https://www.acmicpc.net/problem/10807

import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    nums = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline().rstrip())
    ans = 0
    for i in nums:
        if i == target:
            ans += 1
    print(ans)
    return

if __name__ == "__main__":
    main()