# Problem No.: 1786
# Solver:      Jinmin Goh
# Date:        20200319
# URL: https://www.acmicpc.net/problem/1786

import sys

# KMP algorithm
# good solution: https://bowbowbow.tistory.com/6
# time: O(n + m)

def main():
    T = input()
    P = input()
    ans = []
    pCheck = [0] * len(P)
    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = pCheck[j - 1]
        if P[i] == P[j]:
            pCheck[i] = j + 1
            j += 1
    #print(pCheck)

    j = 0
    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:
            j = pCheck[j - 1]
        #print(i, j)
        if T[i] == P[j]:
            if j == len(P) - 1:
                ans.append(i - len(P) + 2)
                j = pCheck[j]
            else:
                j += 1

    print(len(ans))
    for i in ans:
        print(i, end = " ")
    return

if __name__ == "__main__":
    main()