# Problem No.: 1799
# Solver:      Jinmin Goh
# Date:        20220620
# URL: https://www.acmicpc.net/problem/1799

import sys

def solve(board, n, i, j, cnt):
    if board[i][j] == '0':
        if (i == n - 1 and j == n - 1) or (i == n - 1 and j == n - 2):
            return cnt
        elif j == n - 1:
            if n % 2:
                return solve(board, n, i + 1, 1, cnt)
            else:
                return solve(board, n, i + 1, 0, cnt)
        elif j == n - 2:
            if n % 2:
                return solve(board, n, i + 1, 0, cnt)
            else:
                return solve(board, n, i + 1, 1, cnt)
        else:
            return solve(board, n, i, j + 2, cnt)
    else:
        temp = 0
        # case that didn't located bishop
        if (i == n - 1 and j == n - 1) or (i == n - 1 and j == n - 2):
            temp = cnt
        elif j == n - 1:
            if n % 2:
                temp = solve(board, n, i + 1, 1, cnt)
            else:
                temp = solve(board, n, i + 1, 0, cnt)
        elif j == n - 2:
            if n % 2:
                temp = solve(board, n, i + 1, 0, cnt)
            else:
                temp = solve(board, n, i + 1, 1, cnt)
        else:
            temp = solve(board, n, i, j + 2, cnt)
        # case that located bishop
        board[i][j] = '2'
        flag = False
        # check phase
        for p in range(1, n):
            if i - p < 0 or j - p < 0:
                break
            if board[i - p][j - p] == '2':
                flag = True
                break
        for p in range(1, n):
            if i + p >= n or j + p >= n:
                break
            if board[i + p][j + p] == '2':
                flag = True
                break
        for p in range(1, n):
            if i - p < 0 or j + p >= n:
                break
            if board[i - p][j + p] == '2':
                flag = True
                break
        for p in range(1, n):
            if i + p >= n or j - p < 0:
                break
            if board[i + p][j - p] == '2':
                flag = True
                break
        if not flag:
            if (i == n - 1 and j == n - 1) or (i == n - 1 and j == n - 2):
                temp = max(temp, cnt + 1)
            elif j == n - 1:
                if n % 2:
                    temp = max(temp, solve(board, n, i + 1, 1, cnt + 1))
                else:
                    temp = max(temp, solve(board, n, i + 1, 0, cnt + 1))
            elif j == n - 2:
                if n % 2:
                    temp = max(temp, solve(board, n, i + 1, 0, cnt + 1))
                else:
                    temp = max(temp, solve(board, n, i + 1, 1, cnt + 1))
            else:
                temp = max(temp, solve(board, n, i, j + 2, cnt + 1))
        board[i][j] = '1'
        return temp        

def main():
    n = int(input())
    board = [input().split() for _ in range(n)]
    if n == 1:
        if board[0][0] == '1':
            print(1)
        else:
            print(0)
    else:
        ans = solve(board, n, 0, 0, 0)
        ans += solve(board, n, 0, 1, 0)
        print(ans)
    return

if __name__ == "__main__":
    main()