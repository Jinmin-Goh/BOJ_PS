# Problem No.: 18882
# Solver:      Jinmin Goh
# Date:        20200709
# URL: https://www.acmicpc.net/problem/18882

import sys

def main():
    n, t = map(int, input().split())
    currStatus = input()
    nums = []
    for _ in range(t):
        nums.append(tuple(map(int, sys.stdin.readline().split())))
    nums.sort()

    # only one patient-zero
    # given final state after meeting
    # no midway infection for patient zero; which means patient zero is always initially infected
    # this means at least one patient exists

    # Brute force? -> O(n * t ^ 2)
    pZeroCnt = 0
    kRange = [1000, 0]
    # check for all infected cows
    for i in range(n):
        # pass; not infected
        if currStatus[i] == "0":
            continue
        pZeroFlag = False
        tempRange = []
        # check for all possible k values
        for k in range(252):
            tempStatus = [0] * (n + 1)
            tempStatus[i + 1] = 1
            spreadPatientDict = {}
            # if k > 0; spreadable
            if k != 0:
                spreadPatientDict[i + 1] = k
                # iterate for t inputs
                for p in range(t):
                    x, y = nums[p][1], nums[p][2]
                    # both infected & spreadable
                    if x in spreadPatientDict and y in spreadPatientDict:
                        spreadPatientDict[x] -= 1
                        spreadPatientDict[y] -= 1
                        if spreadPatientDict[x] <= 0:
                            del spreadPatientDict[x]
                        if spreadPatientDict[y] <= 0:
                            del spreadPatientDict[y]
                    # one infected & spreadable
                    elif x in spreadPatientDict:
                        # infecting healthy cow
                        if tempStatus[y] == 0:
                            spreadPatientDict[y] = k
                            tempStatus[y] = 1
                        spreadPatientDict[x] -= 1
                        if spreadPatientDict[x] <= 0:
                            del spreadPatientDict[x]
                    elif y in spreadPatientDict:
                        # infecting healthy cow
                        if tempStatus[x] == 0:
                            spreadPatientDict[x] = k
                            tempStatus[x] = 1
                        spreadPatientDict[y] -= 1
                        if spreadPatientDict[y] <= 0:
                            del spreadPatientDict[y]
            temp = ""
            for p in tempStatus[1:]:
                temp += str(p)
            
            # if satisfies current status
            if temp == currStatus:
                pZeroFlag = True
                tempRange.append(k)
        if pZeroFlag:
            pZeroCnt += 1
            kRange = [min(kRange[0], min(tempRange)), max(kRange[1], max(tempRange))]

    # print phase
    print(pZeroCnt, end = " ")
    if kRange[0] == 251:
        print("Infinity", end = " ")
    else:
        print(kRange[0], end = " ")
    if kRange[1] == 251:
        print("Infinity")
    else:
        print(kRange[1])
    return

if __name__ == "__main__":
    main()