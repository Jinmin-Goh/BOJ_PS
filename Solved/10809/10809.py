# Problem No.: 10809
# Solver:      Jinmin Goh
# Date:        20200308
# URL: https://www.acmicpc.net/problem/10809

import sys

def main():
    word = input()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ans = [-1] * 26
    for i in range(len(alphabet)):
        if alphabet[i] in word:
            ans[i] = word.index(alphabet[i])
    for i in ans:
        print(i, end = " ")
    return

if __name__ == "__main__":
    main()