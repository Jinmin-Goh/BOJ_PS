# Problem No.: 2667
# Solver:      Jinmin Goh
# Date:        20200610
# URL: https://www.acmicpc.net/problem/2667

import sys

def main():
    n = int(input())
    table = []
    for _ in range(n):
        temp = sys.stdin.readline().strip()
        table.append([])
        for i in temp:
            table[-1].append(i)
    
    cnt = 0
    ans = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == "1":
                cnt += 1
                ans.append(0)
                stack = [(i, j)]
                while stack:
                    temp = stack.pop()
                    x, y = temp[0], temp[1]
                    if table[x][y] == "0":
                        continue
                    ans[-1] += 1
                    table[x][y] = "0"
                    if x > 0:
                        stack.append((x - 1, y))
                    if x < n - 1:
                        stack.append((x + 1, y))
                    if y > 0:
                        stack.append((x, y - 1))
                    if y < n - 1:
                        stack.append((x, y + 1))
    ans.sort()
    print(cnt)
    for i in ans:
        print(i)
    return

if __name__ == "__main__":
    main()