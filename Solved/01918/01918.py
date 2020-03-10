# Problem No.: 1918
# Solver:      Jinmin Goh
# Date:        20200310
# URL: https://www.acmicpc.net/problem/1918

import sys

def main():
    string = input()
    if not string:
        print("")
        return
    stack = []
    ans = []
    for i in string:
        if i == "(":
            stack.append(i)
        elif i == ")":
            while stack[-1] != "(":
                ans.append(stack.pop())
            stack.pop()
        elif i in ["*", "/"]:
            if stack:
                while stack and stack[-1] not in ["(", "+", "-", "*", "/"]:
                    ans.append(stack.pop())
                if stack and stack[-1] in ["*", "/"]:
                    ans.append(stack.pop())
            stack.append(i)
        elif i in ["+", "-"]:
            if stack:
                while stack and stack[-1] not in  ["(", "+", "-"]:
                    ans.append(stack.pop())
                if stack and stack[-1] in ["+", "-"]:
                    ans.append(stack.pop())
            stack.append(i)
        else:
            ans.append(i)
    while stack:
        ans.append(stack.pop())
    print("".join(ans))
    return

if __name__ == "__main__":
    main()