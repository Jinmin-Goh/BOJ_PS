# Problem No.: 2239
# Solver:      Jinmin Goh
# Date:        20220615
# URL: https://www.acmicpc.net/problem/2239

from re import T
import sys

def check(sudoku, i, j):
    if sudoku[i][j] == '0':
        for a in range(1, 10):
            n = str(a)
            flag = False
            # row check
            for p in range(9):
                if sudoku[i][p] == n:
                    flag = True
                    break
            # col check
            for p in range(9):
                if sudoku[p][j] == n:
                    flag = True
                    break
            # box check
            for p in range(3):
                for q in range(3):
                    if sudoku[3 * (i // 3) + p][3 * (j // 3) + q] == n:
                        flag = True
                        break
                if flag:
                    break
            if flag:
                continue
            sudoku[i][j] = n
            if check(sudoku, i, j):
                return True
            sudoku[i][j] = '0'
        return False
            
    else:
        if j < 8:
            return check(sudoku, i, j + 1)
        elif i < 8:
            return check(sudoku, i + 1, 0)
        elif i == 8 and j == 8:
            return True 

def main():
    sudoku = []
    for _ in range(9):
        sudoku.append(list(input()))
    check(sudoku, 0, 0)
    for i in sudoku:
        for j in i:
            print(j, end="")
        print()
    return

if __name__ == "__main__":
    main()