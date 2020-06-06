# Problem No.: 1931
# Solver:      Jinmin Goh
# Date:        20200606
# URL: https://www.acmicpc.net/problem/1931

import sys

def main():
    n = int(input())
    timetable = []
    for _ in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        temp = list(reversed(temp))
        timetable.append(temp)
    timetable.sort()
    #print(timetable)
    temp = timetable[0]
    ans = 1
    pos = 1
    while pos < n:
        if timetable[pos][1] < temp[0]:
            pos += 1
            continue
        ans += 1
        temp = timetable[pos]
        #print(timetable[pos], minVal)
        pos += 1
    print(ans)
    return

if __name__ == "__main__":
    main()