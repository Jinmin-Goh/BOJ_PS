# Problem No.: 7568
# Solver:      Jinmin Goh
# Date:        20200313
# URL: https://www.acmicpc.net/problem/7568

import sys

def main():
    n = int(input())
    people = []
    for i in range(n):
        people.append(list(map(int, input().split())))
    for i in range(len(people)):
        ans = 0
        for j in range(len(people)):
            if i == j:
                continue
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                ans += 1
        print(ans + 1, end=" ")
    return

if __name__ == "__main__":
    main()