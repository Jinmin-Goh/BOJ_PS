# Problem No.: 4949
# Solver:      Jinmin Goh
# Date:        20200314
# URL: https://www.acmicpc.net/problem/4949

import sys

def main():
    while True:
        string = input()
        if string == ".":
            break
        stack = []
        flag = True
        for i in string:
            if i == "(" or i == "[":
                stack.append(i)
            elif i == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    flag = False
                    break
            elif i == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    flag = False
                    break
            else:
                continue
        if stack:
            flag = False
        if flag:
            print("yes")
        else:
            print("no")
    return

if __name__ == "__main__":
    main()