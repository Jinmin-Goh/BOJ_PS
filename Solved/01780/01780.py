# Problem No.: 1780
# Solver:      Jinmin Goh
# Date:        20200609
# URL: https://www.acmicpc.net/problem/1780

import sys

def main():
    n = int(input())
    table = []
    for _ in range(n):
        table.append(list(map(int, sys.stdin.readline().split())))
    
    def search(x: int, y: int, length: int) -> [int]:
        if length == 1:
            temp = [0, 0, 0]
            temp[table[x][y] + 1] += 1
            return temp
        num = table[x][y]
        flag = True
        for i in range(length):
            for j in range(length):
                if table[x + i][y + j] != num:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            temp = [0, 0, 0]
            temp[table[x][y] + 1] += 1
            return temp
        else:
            tempAns = [0, 0, 0]
            for i in range(3):
                for j in range(3):
                    temp = search(x + i * (length // 3), y + j * (length // 3), length // 3)
                    tempAns[0] += temp[0]
                    tempAns[1] += temp[1]
                    tempAns[2] += temp[2]
            return tempAns
    ans = search(0, 0, n)
    print(ans[0])
    print(ans[1])
    print(ans[2])
    return

if __name__ == "__main__":
    main()