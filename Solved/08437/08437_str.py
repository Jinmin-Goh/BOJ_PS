# Problem No.: 8437
# Solver:      Jinmin Goh
# Date:        20200525
# URL: https://www.acmicpc.net/problem/8437

import sys

def main():
    a = input()
    b = input()
    
    if a == b:
        print(a)
        print("0")
        return

    # a + b
    sumVal = ""
    carry = 0
    for i in range(len(b)):
        temp = carry + int(a[-i - 1]) + int(b[-i - 1])
        sumVal = str(temp % 10) + sumVal
        carry = temp // 10
    appendVal = a[:-len(b)]
    if appendVal and (carry + int(appendVal[-1])) >= 10:
        cnt = 1
        temp = ""
        while carry and cnt <= len(appendVal):
            temp = str((int(appendVal[-cnt]) + carry) % 10) + temp
            carry = (int(appendVal[-cnt]) + carry) // 10
            cnt += 1
        if cnt > len(appendVal) and carry:
            temp = "1" + temp
            appendVal = temp
        if cnt <= len(appendVal):
            appendVal = appendVal[:-len(temp)] + temp
    elif not appendVal and carry:
        appendVal = "1" + appendVal
    else:
        if appendVal:
            appendVal = appendVal[:-1] + str(int(appendVal[-1]) + carry)
    sumVal = appendVal + sumVal
    
    # (a + b) // 2 -> newA
    newA = ""
    carry = 0
    for i in sumVal:
        newA += str(int(i) // 2 + carry)
        if int(i) % 2:
            carry = 5
        else:
            carry = 0
    if newA[0] == "0":
        newA = newA[1:]
    
    # a - (a + b) // 2 -> newB
    newB = ""
    carry = 0
    for i in range(len(newA)):
        if int(a[-i - 1]) < int(newA[-i - 1]) + carry:
            newB = str(int(a[-i - 1]) + 10 - int(newA[-i - 1]) - carry) + newB
            carry = 1
        else:
            newB = str(int(a[-i - 1]) - int(newA[-i - 1]) - carry) + newB
            carry = 0
    appendVal = a[:-len(newA)]
    if carry:
        temp = ""
        cnt = 1
        while carry:
            if appendVal[-cnt] == "0":
                temp = "9" + temp
                carry = 1
            else:
                temp = str(int(appendVal[-cnt]) - carry) + temp
                carry = 0
            cnt += 1
        appendVal = temp
    newB = appendVal + newB
    while newB[0] == "0":
        newB = newB[1:]
    print(newA)
    print(newB)
    return

if __name__ == "__main__":
    main()