# Problem No.: 19844
# Solver:      Jinmin Goh
# Date:        20200914
# URL: https://www.acmicpc.net/problem/19844

import sys

def main():
    inputStr = input()
    ansList = list(inputStr.split())
    for i in range(5100):
        #print(ansList)
        if i >= len(ansList):
            break
        ansList = ansList[:i] + list(ansList[i].split("-")) + ansList[i + 1:]
    #print(ansList)
    
    front = ["c", "j", "n", "m", "t", "s", "l", "d", "qu"]
    vowel = ["a", "e", "i", "o", "u", "h"]
    ans = len(ansList)
    for string in ansList:
        #print(string)
        if "'" in string:
            temp = list(string.split("'"))
            if temp[0] in front and temp[1][0] in vowel:
                ans += 1
    print(ans)
    return

if __name__ == "__main__":
    main()