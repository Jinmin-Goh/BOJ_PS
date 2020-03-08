# Problem No.: 1157
# Solver:      Jinmin Goh
# Date:        20200308
# URL: https://www.acmicpc.net/problem/1157

import sys

def main():
    word = input().upper()
    wordDict = {}
    for i in word:
        if i not in wordDict:
            wordDict[i] = 1
        else:
            wordDict[i] += 1
    maxVal = 0
    ans = ""
    for i in wordDict:
        if maxVal < wordDict[i]:
            maxVal = wordDict[i]
            ans = i
    for i in wordDict:
        if i != ans and wordDict[i] == maxVal:
            print("?")
            return
    print(ans)
    return

if __name__ == "__main__":
    main()