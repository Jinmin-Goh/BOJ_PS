# Problem No.: 17143
# Solver:      Jinmin Goh
# Date:        20220627
# URL: https://www.acmicpc.net/problem/17143

import sys

def main():
    R, C, M = map(int, input().split())
    map_table = [[-1 for _ in range(C)] for __ in range(R)]
    sharks = []
    for i in range(M):
        r, c, s, d, z = map(int, sys.stdin.readline().split())
        map_table[r - 1][c - 1] = i
        sharks.append([r - 1, c - 1, s, d, z])
    ans = 0
    pos = 0
    for _ in range(C):
        # catch shark
        target = None
        for i in range(R):
            if map_table[i][pos] != -1:
                target = map_table[i][pos]
                break
        if target != None:
            ans += sharks[target][4]
            sharks[target] = []
        after_table = [[-1 for _ in range(C)] for __ in range(R)]
        # move shark
        for i in range(M):
            if sharks[i] == []:
                continue
            r, c, s, d, z = sharks[i]
            r_temp = r
            c_temp = c
            if d == 1:
                if r >= s:
                    r_temp = r - s
                else:
                    s -= r
                    if (s // (R - 1)) % 2:
                        r_temp = R - 1 - s % (R - 1)
                    else:
                        r_temp = s % (R - 1)
                        sharks[i][3] = 2
            elif d == 2:
                if R - 1 - r >= s:
                    r_temp = r + s
                else:
                    s -= R - 1 - r
                    if (s // (R - 1)) % 2:
                        r_temp = s % (R - 1)
                    else:
                        r_temp = R - 1 - s % (R - 1)
                        sharks[i][3] = 1
            elif d == 3:
                if C - 1 - c >= s:
                    c_temp = c + s
                else:
                    s -= C - 1 - c
                    if (s // (C - 1)) % 2:
                        c_temp = s % (C - 1)
                    else:
                        c_temp = C - 1 - s % (C - 1)
                        sharks[i][3] = 4
            elif d == 4:
                if c >= s:
                    c_temp = c - s
                else:
                    s -= c
                    if (s // (C - 1)) % 2:
                        c_temp = C - 1 - s % (C - 1)
                    else:
                        c_temp = s % (C - 1)
                        sharks[i][3] = 3
            temp = after_table[r_temp][c_temp]
            if temp == -1:  # no collision
                after_table[r_temp][c_temp] = i
                sharks[i][0] = r_temp
                sharks[i][1] = c_temp
            else:   # collision
                if sharks[temp][4] > sharks[i][4]:
                    sharks[i] = []
                else:
                    sharks[temp] = []
                    after_table[r_temp][c_temp] = i
                    sharks[i][0] = r_temp
                    sharks[i][1] = c_temp
        map_table = after_table
        # move right
        pos += 1
    print(ans)
    return

if __name__ == "__main__":
    main()