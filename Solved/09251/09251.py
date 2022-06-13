# Problem No.: 9251
# Solver:      Jinmin Goh
# Date:        20220614
# URL: https://www.acmicpc.net/problem/9251

import sys

def main():
    word1 = input()
    word2 = input()
    dpTable = [[0 for _ in range(len(word2) + 1)] for i in range(len(word1) + 1)]
    ans = 0
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                dpTable[i][j] = dpTable[i - 1][j - 1] + 1
                if ans < dpTable[i][j]:
                    ans = dpTable[i][j]
            else:
                dpTable[i][j] = max(dpTable[i][j - 1], dpTable[i - 1][j])
    print(ans)
    return

if __name__ == "__main__":
    main()