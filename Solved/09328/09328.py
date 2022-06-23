# Problem No.: 9328
# Solver:      Jinmin Goh
# Date:        20220623
# URL: https://www.acmicpc.net/problem/9328

import sys

def main():
    t = int(input())
    for _ in range(t):
        # input parsing
        n, m = map(int, sys.stdin.readline().split())
        table = [list(sys.stdin.readline()) for __ in range(n)]
        keys = set(sys.stdin.readline().rstrip())
        # find start point
        start = []
        for i in range(n):
            for j in range(m):
                if i != 0 and i != n - 1 and j != 0 and j != m - 1:
                    continue
                if table[i][j] != '*':
                    start .append((i, j))
        # BFS
        queue = start
        visited = [[False for __ in range(m)] for ___ in range(n)]
        locks = {}
        ans = 0
        while queue:
            temp = []
            for row, col in queue:
                if visited[row][col]:
                    continue
                if table[row][col] == '.':
                    visited[row][col] = True
                elif table[row][col] == '$':
                    ans += 1
                    table[row][col] = '.'
                    visited[row][col] = True
                elif table[row][col] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    if table[row][col].lower() not in keys:
                        if table[row][col] not in locks:
                            locks[table[row][col]] = []
                        locks[table[row][col]].append((row, col))
                        visited[row][col] = True
                        continue
                    else:
                        table[row][col] = '.'
                        visited[row][col] = True
                elif table[row][col] in 'abcdefghijklmnopqrstuvwxyz':
                    keys.add(table[row][col])
                    if table[row][col].upper() in locks:
                        temp += locks[table[row][col].upper()]
                        for pos in locks[table[row][col].upper()]:
                            visited[pos[0]][pos[1]] = False
                    table[row][col] = '.'
                    visited[row][col] = True
                else:
                    continue
                if row > 0 and not visited[row - 1][col] and table[row - 1][col] != '*':
                    temp.append((row - 1, col))
                if row < n - 1 and not visited[row + 1][col] and table[row + 1][col] != '*':
                    temp.append((row + 1, col))
                if col > 0 and not visited[row][col - 1] and table[row][col - 1] != '*':
                    temp.append((row, col - 1))
                if col < m - 1 and not visited[row][col + 1] and table[row][col + 1] != '*':
                    temp.append((row, col + 1))
            queue = temp
        print(ans)

    return

if __name__ == "__main__":
    main()