# Problem No.: 3033
# Solver:      Jinmin Goh
# Date:        20200621
# URL: https://www.acmicpc.net/problem/3033

import sys
import collections

def main():
    n = int(input())
    S = input()

    # appropriate prime
    modVal = 2147483647
    powVal = 256

    def RabinKarp() -> bool:
        if pMid == 0:
            return True
        tempVal = 0
        for i in range(pMid):
            tempVal = (tempVal * powVal + ord(S[i])) % modVal

        mulVal = (1 << (8 * (pMid - 1))) % modVal
                    
        hashDict = collections.defaultdict(list)
        hashDict[tempVal].append(0)
        
        for i in range(len(S) - pMid):
            tempVal = ((tempVal - ord(S[i]) * mulVal) * powVal + ord(S[i + pMid])) % modVal
            for j in hashDict[tempVal]:
                if S[i + 1:i + pMid + 1] == S[j:j + pMid]:
                    return True
            hashDict[tempVal].append(i + 1)
        return False

    # binary search
    pFront = 0
    pRear = len(S)
    while pFront + 1 < pRear:
        pMid = (pFront + pRear) // 2    
        flag = RabinKarp()
        if flag:
            pFront = pMid
        else:
            pRear = pMid
    print(pFront)
    return

if __name__ == "__main__":
    main()