# Problem No.: 15829
# Solver:      Jinmin Goh
# Date:        20200317
# URL: https://www.acmicpc.net/problem/15829

import sys

def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetDict = {}
    cnt = 1
    for i in alphabet:
        alphabetDict[i] = cnt
        cnt += 1
    n = int(input())
    string = input()
    sum = 0
    for i in range(n):
        sum += (alphabetDict[string[i]] * (31 ** i)) % 1234567891
    print(sum % 1234567891)
    return

if __name__ == "__main__":
    main()