# Problem No.: 10942
# Solver:      Jinmin Goh
# Date:        20200311
# URL: https://www.acmicpc.net/problem/10942

import sys

def main():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    palindromeSet = set()
    
    for i in range(n):
        # odd palindrome
        temp = 0
        while i - temp >= 0 and i + temp < n:
            if nums[i - temp] == nums[i + temp]:
                palindromeSet.add((i - temp, i + temp))
                temp += 1
            else:
                break
        # even palindrome
        temp = 0
        while i - temp >= 0 and i + 1 + temp < n:
            if nums[i - temp] == nums[i + 1 + temp]:
                palindromeSet.add((i - temp, i + 1 + temp))
                temp += 1
            else:
                break
    m = int(sys.stdin.readline())
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if (a - 1, b - 1) in palindromeSet:
            print(1)
        else:
            print(0)
    return

if __name__ == "__main__":
    main()