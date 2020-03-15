# Problem No.: 5430
# Solver:      Jinmin Goh
# Date:        20200314
# URL: https://www.acmicpc.net/problem/5430

import sys

def main():
    T = int(input())
    for i in range(T):
        string = input()
        n = int(input())
        temp = input()
        if n == 0:
            stack = []
        else:
            stack = list(map(int, temp[1:-1].split(",")))
        errorFlag = False
        revFlag = False
        j = 0
        while j < len(string):
            if string[j] == "R":
                if j < len(string) - 1 and string[j + 1] == "R":
                    j += 2
                    continue
                elif len(stack) <= 1:
                    j += 1
                    continue
                revFlag = not revFlag
            elif string[j] == "D":
                if not stack:
                    errorFlag = True
                    break
                else:
                    if revFlag:
                        stack.pop()
                    else:
                        stack.pop(0)
            j += 1
        if errorFlag:
            print("error")
        else:
            if revFlag:
                temp = []
                while stack:
                    temp.append(stack.pop())
                stack = temp[:]
            if not stack:
                print("[]")
            else:
                ans = "["
                for j in stack:
                    ans += str(j) + ","
                ans = ans[:-1] + "]"
                print(ans)
    return

if __name__ == "__main__":
    main()