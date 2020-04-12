# Problem No.: 1541
# Solver:      Jinmin Goh
# Date:        20200413
# URL: https://www.acmicpc.net/problem/1541

import sys

def main():
    string = input()
    temp = ""
    nums = []
    ops = []
    for i in string:
        if i not in ["+", "-"]:
            temp += i
        else:
            nums.append(int(temp))
            ops.append(i)
            temp = ""
    nums.append(int(temp))
    #print(nums, ops)
    ans = nums.pop(0)
    while ops:
        if ops[0] == "-":
            break
        else:
            ans += nums.pop(0)
            ops.pop(0)
    temp = 0
    while ops:
        if ops[0] == "-":
            ops.pop(0)
            temp += nums.pop(0)
            while ops and ops[0] != "-":
                temp += nums.pop(0)
                ops.pop(0)
            ans -= temp
            temp = 0
    print(ans)
    return

if __name__ == "__main__":
    main()