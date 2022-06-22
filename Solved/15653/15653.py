# Problem No.: 15653
# Solver:      Jinmin Goh
# Date:        20220622
# URL: https://www.acmicpc.net/problem/15653

import sys

def move(table, path, R_pos, B_pos, temp_queue, direction):
    for dir in direction:
        if dir == path:
            continue
        temp = dir
        new_R_pos = None
        new_B_pos = None
        flag = None
        if dir == 'L':
            # R, B both in same row
            if R_pos[0] == B_pos[0]:
                # R is at the left side of B
                if R_pos[1] < B_pos[1]:
                    # move R first
                    for i in range(R_pos[1] - 1, -1, -1):
                        # if meets wall; stop
                        if table[R_pos[0]][i] == '#':
                            new_R_pos = (R_pos[0], i + 1)
                            break
                        # if meets hole; stop
                        elif table[R_pos[0]][i] == 'O':
                            new_R_pos = (R_pos[0], i)
                            flag = True
                            break
                        else:
                            new_R_pos = (R_pos[0], i)
                    # move B last
                    for i in range(B_pos[1] - 1, -1, -1):
                        # if meets wall; stop
                        if table[B_pos[0]][i] == '#':
                            new_B_pos = (B_pos[0], i + 1)
                            break
                        # if meets hole; failure
                        elif table[B_pos[0]][i] == 'O':
                            flag = False
                            break
                        # if meets R; stop
                        elif i == new_R_pos[1]:
                            new_B_pos = (B_pos[0], i + 1)
                            break
                        else:
                            new_B_pos = (B_pos[0], i)
                # R is at the right side of B
                else:
                    # move B first
                    for i in range(B_pos[1] - 1, -1, -1):
                        # if meets wall; stop
                        if table[B_pos[0]][i] == '#':
                            new_B_pos = (B_pos[0], i + 1)
                            break
                        # if meets hole; failure
                        elif table[B_pos[0]][i] == 'O':
                            new_B_pos = (B_pos[0], i)
                            flag = False
                            break
                        else:
                            new_B_pos = (B_pos[0], i)
                    if flag == False:
                        continue
                    # move R last
                    for i in range(R_pos[1] - 1, -1, -1):
                        # if meets wall; stop
                        if table[R_pos[0]][i] == '#':
                            new_R_pos = (R_pos[0], i + 1)
                            break
                        # if meets hole; failure
                        elif table[R_pos[0]][i] == 'O':
                            flag = True
                            break
                        # if meets B; stop
                        elif i == new_B_pos[1]:
                            new_R_pos = (R_pos[0], i + 1)
                            break
                        else:
                            new_R_pos = (R_pos[0], i)
            # R, B at different row
            else:
                # move R
                for i in range(R_pos[1] - 1, -1, -1):
                    # if meets wall; stop
                    if table[R_pos[0]][i] == '#':
                        new_R_pos = (R_pos[0], i + 1)
                        break
                    # if meets hole; success
                    elif table[R_pos[0]][i] == 'O':
                        flag = True
                        break
                    else:
                        new_R_pos = (R_pos[0], i)
                # move B
                for i in range(B_pos[1] - 1, -1, -1):
                    # if meets wall; stop
                    if table[B_pos[0]][i] == '#':
                        new_B_pos = (B_pos[0], i + 1)
                        break
                    # if meets hole; failure
                    elif table[B_pos[0]][i] == 'O':
                        flag = False
                        break
                    else:
                        new_B_pos = (B_pos[0], i)
        elif dir == 'R':
            # R, B both in same row
            if R_pos[0] == B_pos[0]:
                # R is at the right side of B
                if R_pos[1] > B_pos[1]:
                    # move R first
                    for i in range(R_pos[1] + 1, len(table[0])):
                        # if meets wall; stop
                        if table[R_pos[0]][i] == '#':
                            new_R_pos = (R_pos[0], i - 1)
                            break
                        # if meets hole; stop
                        elif table[R_pos[0]][i] == 'O':
                            new_R_pos = (R_pos[0], i)
                            flag = True
                            break
                        else:
                            new_R_pos = (R_pos[0], i)
                    # move B last
                    for i in range(B_pos[1] + 1, len(table[0])):
                        # if meets wall; stop
                        if table[B_pos[0]][i] == '#':
                            new_B_pos = (B_pos[0], i - 1)
                            break
                        # if meets hole; failure
                        elif table[B_pos[0]][i] == 'O':
                            flag = False
                            break
                        # if meets R; stop
                        elif i == new_R_pos[1]:
                            new_B_pos = (B_pos[0], i - 1)
                            break
                        else:
                            new_B_pos = (B_pos[0], i)
                # R is at the left side of B
                else:
                    # move B first
                    for i in range(B_pos[1] + 1, len(table[0])):
                        # if meets wall; stop
                        if table[B_pos[0]][i] == '#':
                            new_B_pos = (B_pos[0], i - 1)
                            break
                        # if meets hole; failure
                        elif table[B_pos[0]][i] == 'O':
                            new_B_pos = (B_pos[0], i)
                            flag = False
                            break
                        else:
                            new_B_pos = (B_pos[0], i)
                    if flag == False:
                        continue
                    # move R last
                    for i in range(R_pos[1] + 1, len(table[0])):
                        # if meets wall; stop
                        if table[R_pos[0]][i] == '#':
                            new_R_pos = (R_pos[0], i - 1)
                            break
                        # if meets hole; stop
                        elif table[R_pos[0]][i] == 'O':
                            flag = True
                            break
                        # if meets B; stop
                        elif i == new_B_pos[1]:
                            new_R_pos = (R_pos[0], i - 1)
                            break
                        else:
                            new_R_pos = (R_pos[0], i)
            # R, B at different row
            else:
                # move R
                for i in range(R_pos[1] + 1, len(table[0])):
                    # if meets wall; stop
                    if table[R_pos[0]][i] == '#':
                        new_R_pos = (R_pos[0], i - 1)
                        break
                    # if meets hole; success
                    elif table[R_pos[0]][i] == 'O':
                        flag = True
                        break
                    else:
                        new_R_pos = (R_pos[0], i)
                # move B
                for i in range(B_pos[1] + 1, len(table[0])):
                    # if meets wall; stop
                    if table[B_pos[0]][i] == '#':
                        new_B_pos = (B_pos[0], i - 1)
                        break
                    # if meets hole; failure
                    elif table[B_pos[0]][i] == 'O':
                        flag = False
                        break
                    else:
                        new_B_pos = (B_pos[0], i)
        elif dir == 'U':
            # R, B both in same column
            if R_pos[1] == B_pos[1]:
                # R is at the upper side of B
                if R_pos[0] < B_pos[0]:
                    # move R first
                    for i in range(R_pos[0] - 1, -1, -1):
                        # if meets wall; stop
                        if table[i][R_pos[1]] == '#':
                            new_R_pos = (i + 1, R_pos[1])
                            break
                        # if meets hole; stop
                        elif table[i][R_pos[1]] == 'O':
                            new_R_pos = (i, R_pos[1])
                            flag = True
                            break
                        else:
                            new_R_pos = (i, R_pos[1])
                    # move B last
                    for i in range(B_pos[0] - 1, -1, -1):
                        # if meets wall; stop
                        if table[i][B_pos[1]] == '#':
                            new_B_pos = (i + 1, B_pos[1])
                            break
                        # if meets hole; failure
                        elif table[i][B_pos[1]] == 'O':
                            flag = False
                            break
                        # if meets R; stop
                        elif i == new_R_pos[0]:
                            new_B_pos = (i + 1, B_pos[1])
                            break
                        else:
                            new_B_pos = (i, B_pos[1])
                # R is at the lower side of B
                else:
                    # move B first
                    for i in range(B_pos[0] - 1, -1, -1):
                        # if meets wall; stop
                        if table[i][B_pos[1]] == '#':
                            new_B_pos = (i + 1, B_pos[1])
                            break
                        # if meets hole; failure
                        elif table[i][B_pos[1]] == 'O':
                            new_B_pos = (i, B_pos[1])
                            flag = False
                            break
                        else:
                            new_B_pos = (i, B_pos[1])
                    if flag == False:
                        continue
                    # move R last
                    for i in range(R_pos[0] - 1, -1, -1):
                        # if meets wall; stop
                        if table[i][R_pos[1]] == '#':
                            new_R_pos = (i + 1, R_pos[1])
                            break
                        # if meets hole;
                        elif table[i][R_pos[1]] == 'O':
                            flag = True
                            break
                        # if meets R; stop
                        elif i == new_B_pos[0]:
                            new_R_pos = (i + 1, R_pos[1])
                            break
                        else:
                            new_R_pos = (i, R_pos[1])
            # R, B at different column
            else:
                # move R
                for i in range(R_pos[0] - 1, -1, -1):
                    # if meets wall; stop
                    if table[i][R_pos[1]] == '#':
                        new_R_pos = (i + 1, R_pos[1])
                        break
                    # if meets hole; stop
                    elif table[i][R_pos[1]] == 'O':
                        flag = True
                        break
                    else:
                        new_R_pos = (i, R_pos[1])
                # move B
                for i in range(B_pos[0] - 1, -1, -1):
                    # if meets wall; stop
                    if table[i][B_pos[1]] == '#':
                        new_B_pos = (i + 1, B_pos[1])
                        break
                    # if meets hole; failure
                    elif table[i][B_pos[1]] == 'O':
                        flag = False
                        break
                    else:
                        new_B_pos = (i, B_pos[1])
        elif dir == 'D':
            # R, B both in same column
            if R_pos[1] == B_pos[1]:
                # R is at the lower side of B
                if R_pos[0] > B_pos[0]:
                    # move R first
                    for i in range(R_pos[0] + 1, len(table)):
                        # if meets wall; stop
                        if table[i][R_pos[1]] == '#':
                            new_R_pos = (i - 1, R_pos[1])
                            break
                        # if meets hole; stop
                        elif table[i][R_pos[1]] == 'O':
                            new_R_pos = (i, R_pos[1])
                            flag = True
                            break
                        else:
                            new_R_pos = (i, R_pos[1])
                    # move B last
                    for i in range(B_pos[0] + 1, len(table)):
                        # if meets wall; stop
                        if table[i][B_pos[1]] == '#':
                            new_B_pos = (i - 1, B_pos[1])
                            break
                        # if meets hole; failure
                        elif table[i][B_pos[1]] == 'O':
                            flag = False
                            break
                        # if meets R; stop
                        elif i == new_R_pos[0]:
                            new_B_pos = (i - 1, B_pos[1])
                            break
                        else:
                            new_B_pos = (i, B_pos[1])
                # R is at the upper side of B
                else:
                    # move B first
                    for i in range(B_pos[0] + 1, len(table)):
                        # if meets wall; stop
                        if table[i][B_pos[1]] == '#':
                            new_B_pos = (i - 1, B_pos[1])
                            break
                        # if meets hole; failure
                        elif table[i][B_pos[1]] == 'O':
                            new_B_pos = (i, B_pos[1])
                            flag = False
                            break
                        else:
                            new_B_pos = (i, B_pos[1])
                    if flag == False:
                        continue
                    # move R last
                    for i in range(R_pos[0] + 1, len(table)):
                        # if meets wall; stop
                        if table[i][R_pos[1]] == '#':
                            new_R_pos = (i - 1, R_pos[1])
                            break
                        # if meets hole; failure
                        elif table[i][R_pos[1]] == 'O':
                            flag = True
                            break
                        # if meets R; stop
                        elif i == new_B_pos[0]:
                            new_R_pos = (i - 1, R_pos[1])
                            break
                        else:
                            new_R_pos = (i, R_pos[1])
            # R, B at different column
            else:
                # move R
                for i in range(R_pos[0] + 1, len(table)):
                    # if meets wall; stop
                    if table[i][R_pos[1]] == '#':
                        new_R_pos = (i - 1, R_pos[1])
                        break
                    # if meets hole; stop
                    elif table[i][R_pos[1]] == 'O':
                        flag = True
                        break
                    else:
                        new_R_pos = (i, R_pos[1])
                # move B
                for i in range(B_pos[0] + 1, len(table)):
                    # if meets wall; stop
                    if table[i][B_pos[1]] == '#':
                        new_B_pos = (i - 1, B_pos[1])
                        break
                    # if meets hole; failure
                    elif table[i][B_pos[1]] == 'O':
                        flag = False
                        break
                    else:
                        new_B_pos = (i, B_pos[1])
        
        # if marble didn't move
        if new_R_pos == R_pos and new_B_pos == B_pos:
            continue
        # if R reached hole
        if flag == True:
            return temp
        # if no marble reached hole
        if flag == None:
            temp_queue.append((temp, new_R_pos, new_B_pos))
    return None

def main():
    # input parsing
    n, m = map(int, input().split())
    table = [list(input()) for _ in range(n)]
    # R, B pos finding
    R_pos = None
    B_pos = None
    for i in range(n):
        for j in range(m):
            if table[i][j] == 'R':
                R_pos = (i, j)
                table[i][j] = '.'
            if table[i][j] == 'B':
                B_pos = (i, j)
                table[i][j] = '.'
    # BFS
    queue = [(None, R_pos, B_pos)]
    direction = ['L', 'R', 'U', 'D']
    ans = None
    cnt = 0
    pos_set = set()
    while queue:
        temp = []
        for path, R, B in queue:
            if (R, B) in pos_set:
                continue
            pos_set.add((R, B))
            ans = move(table, path, R, B, temp, direction)
            if ans != None:
                break
        cnt += 1
        if ans != None:
            break
        queue = temp
    if ans != None:
        print(cnt)
    else:
        print(-1)
    return

if __name__ == "__main__":
    main()