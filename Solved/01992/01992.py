# Problem No.: 1992
# Solver:      Jinmin Goh
# Date:        20200610
# URL: https://www.acmicpc.net/problem/1992

import sys

def main():
    n = int(input())
    table = []
    for _ in range(n):
        table.append(sys.stdin.readline().strip())
    
    def search(x: int, y: int, length: int) -> int:
        if length == 1:
            return table[x][y]
        num = table[x][y]
        flag = False
        for i in range(length):
            for j in range(length):
                if table[x + i][y + j] != num:
                    flag = True
                    break
            if flag:
                break
        if flag:
            temp = "("
            for i in range(2):
                for j in range(2):
                    temp += search(x + i * (length // 2), y + j * (length // 2), length // 2)
            temp += ")"
        else:
            temp = num
        return temp
    ans = search(0, 0, n)
    print(ans)


    return

if __name__ == "__main__":
    main()