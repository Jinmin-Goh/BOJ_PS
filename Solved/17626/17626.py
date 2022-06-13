# Problem No.: 17626
# Solver:      Jinmin Goh
# Date:        20200410
# URL: https://www.acmicpc.net/problem/17626

import sys

def main():
    n = int(input())
    nList = [4 for _ in range(50001)]
    for i in range(1, int(50000 ** 0.5) + 1):
        if i ** 2 > 50000:
            break
        nList[i ** 2] = 1
    for i in range(1, int(50000 ** 0.5) + 1):
        for j in range(1, int(50000 ** 0.5) + 1):
            if i ** 2 + j ** 2 > 50000:
                break
            nList[i ** 2 + j ** 2] = min(nList[i ** 2 + j ** 2], 2)
    for i in range(1, int(50000 ** 0.5) + 1):
        for j in range(1, int(50000 ** 0.5) + 1):
            for k in range(1, int(50000 ** 0.5) + 1):
                if i ** 2 + j ** 2 + k ** 2 > 50000:
                    break
                nList[i ** 2 + j ** 2 + k ** 2] = min(nList[i ** 2 + j ** 2 + k ** 2], 3)
    print(nList[n])
    return
    
if __name__ == "__main__":
    main()