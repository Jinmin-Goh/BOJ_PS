# Problem No.: 9251
# Solver:      Jinmin Goh
# Date:        20200310
# URL: https://www.acmicpc.net/problem/9251

import sys

def main():
    word1 = input()
    word2 = input()
    dpTable = [[0] * len(word2) for i in range(len(word1))]
    for i in range(len(word1)):
        for j in range(len(word2)):
            if word1[i] == word2[j]:
                if j == 0:
                    dpTable[i][j] = 1
                else:
                    dpTable[i][j] = max(dpTable[i - 1][:j]) + 1
            else:
                if j == 0:
                    if i == 0:
                        dpTable[i][j] = 0
                    else:
                        dpTable[i][j] = dpTable[i - 1][j]
                else:
                    dpTable[i][j] = max(dpTable[i][j - 1], dpTable[i - 1][j])
    print(dpTable[-1][-1])
    return

if __name__ == "__main__":
    main()