# Problem No.: 1181
# Solver:      Jinmin Goh
# Date:        20200309
# URL: https://www.acmicpc.net/problem/1181

import sys

def main():
    n = int(input())
    wordSet = set()
    wordList = []
    for i in range(n):
        word = input()
        if word not in wordSet:
            wordList.append((len(word), word))
            wordSet.add(word)
    wordList.sort()
    for i in wordList:
        print(i[1])
    return

if __name__ == "__main__":
    main()