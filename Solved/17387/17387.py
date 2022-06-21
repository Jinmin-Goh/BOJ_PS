# Problem No.: 17387
# Solver:      Jinmin Goh
# Date:        20220621
# URL: https://www.acmicpc.net/problem/17387

import sys

def ccw(x1, y1, x2, y2, x3, y3):
    val = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if val > 0:
        return 1
    elif val == 0:
        return 0
    else:
        return -1

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    val_123 = ccw(x1, y1, x2, y2, x3, y3)
    val_124 = ccw(x1, y1, x2, y2, x4, y4)
    val_341 = ccw(x3, y3, x4, y4, x1, y1)
    val_342 = ccw(x3, y3, x4, y4, x2, y2)
    if val_123 == 0 and val_124 == 0 and val_341 == 0 and val_342 == 0:
        if min(x1, x2) <= max(x3, x4) and\
            min(x3, x4) <= max(x1, x2) and\
            min(y1, y2) <= max(y3, y4) and\
            min(y3, y4) <= max(y1, y2):
            print(1)
        else:
            print(0)
    elif val_123 * val_124 <= 0 and val_341 * val_342 <= 0:
        print(1)
    else:
        print(0)
    
    return

if __name__ == "__main__":
    main()