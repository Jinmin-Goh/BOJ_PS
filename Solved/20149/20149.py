# Problem No.: 20149
# Solver:      Jinmin Goh
# Date:        20220805
# URL: https://www.acmicpc.net/problem/20149

import sys

def ccw(x1, y1, x2, y2, x3, y3):
    val = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if val > 0:
        return 1
    elif val < 0:
        return -1
    else:
        return 0

def main():
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
    if (x1, y1) > (x2, y2):
        x1, y1, x2, y2 = x2, y2, x1, y1
    if (x3, y3) > (x4, y4):
        x3, y3, x4, y4 = x4, y4, x3, y3
    val1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    val2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
    if val1 <= 0 and val2 <= 0 and (x1, y1) <= (x4, y4) and (x2, y2) >= (x3, y3):
        print(1)
        if (y2 - y1) * (x4 - x3) == (x2 - x1) * (y4 - y3):
            if x1 == x2:
                if y1 < y4 and y2 == y3:
                    print(x2, y2)
                elif y1 == y4 and y2 > y3:
                    print(x1, y1)
            else:
                if x1 < x4 and x2 == x3:
                    print(x2, y2)
                elif x1 == x4 and x2 > x3:
                    print(x1, y1)
        else:
            if x1 == x2:
                a2 = (y4 - y3) / (x4 - x3)
                b2 = y3 - a2 * x3
                x = x1
                y = a2 * x + b2
                print(x, y)    
            elif x3 == x4:
                a1 = (y2 - y1) / (x2 - x1)
                b1 = y1 - a1 * x1
                x = x3
                y = a1 * x + b1
                print(x, y)    
            else:
                a1 = (y2 - y1) / (x2 - x1)
                b1 = y1 - a1 * x1
                a2 = (y4 - y3) / (x4 - x3)
                b2 = y3 - a2 * x3
                x = (b2 - b1) / (a1 - a2)
                y = a1 * x + b1
                print(x, y)    
    else:
        print(0)
    return

if __name__ == "__main__":
    main()