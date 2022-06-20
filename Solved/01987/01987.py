# Problem No.: 1987
# Solver:      Jinmin Goh
# Date:        20220620
# URL: https://www.acmicpc.net/problem/1987

import sys

def solve(board, visited, visited_list, row, col, cnt):
    if visited_list[ord(board[row][col]) - ord('A')] or visited[row][col]:
        return cnt
    visited[row][col] = True
    visited_list[ord(board[row][col]) - ord('A')] = True
    temp = 0
    if row > 0:
        if visited_list[ord(board[row - 1][col]) - ord('A')] or visited[row - 1][col]:
            temp = max(temp, cnt + 1)
        else:
            temp = max(temp, solve(board, visited, visited_list, row - 1, col, cnt + 1))
    if row < len(board) - 1:
        if visited_list[ord(board[row + 1][col]) - ord('A')] or visited[row + 1][col]:
            temp = max(temp, cnt + 1)
        else:
            temp = max(temp, solve(board, visited, visited_list, row + 1, col, cnt + 1))
    if col > 0:
        if visited_list[ord(board[row][col - 1]) - ord('A')] or visited[row][col - 1]:
            temp = max(temp, cnt + 1)
        else:
            temp = max(temp, solve(board, visited, visited_list, row, col - 1, cnt + 1))
    if col < len(board[0]) - 1:
        if visited_list[ord(board[row][col + 1]) - ord('A')] or visited[row][col + 1]:
            temp = max(temp, cnt + 1)
        else:
            temp = max(temp, solve(board, visited, visited_list, row, col + 1, cnt + 1))
    visited[row][col] = False
    visited_list[ord(board[row][col]) - ord('A')] = False
    return temp

def main():
    r, c = map(int, input().split())
    board = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
    visited = [[False for _ in range(c)] for __ in range(r)]
    visited_list = [False for _ in range(26)]
    ans = solve(board, visited, visited_list, 0, 0, 0)
    print(ans)
    return

if __name__ == "__main__":
    main()