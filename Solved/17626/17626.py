# Problem No.: 17626
# Solver:      Jinmin Goh
# Date:        20200410
# URL: https://www.acmicpc.net/problem/17626

import sys

def main():
    n = int(input())
    if (int(n ** 0.5)) ** 2 == n:
        print(1)
        return
    for i in reversed(range(1, int(n ** 0.5) + 1)):
        if i ** 2 < n // 2:
            break
        temp = n - i ** 2
        if (int(temp ** 0.5)) ** 2 == temp:
            print(2)
            return
    for i in reversed(range(1, int(n ** 0.5) + 1)):
        if i ** 2 < n // 2:
            break
        temp1 = n - i ** 2
        for j in reversed(range(1, int(temp1 ** 0.5) + 1)):
            if j ** 2 < temp1 // 2:
                break
            temp2 = temp1 - j ** 2
            if (int(temp2 ** 0.5)) ** 2 == temp2:
                print(3)
                return
    print(4)
    return
    
if __name__ == "__main__":
    main()