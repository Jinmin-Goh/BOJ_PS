# Problem No.: 25399
# Solver:      Jinmin Goh
# Date:        20220803
# URL: https://www.acmicpc.net/problem/25399

import sys, math

def main():
    n = int(sys.stdin.readline().rstrip())
    negative = False
    if n < 0:
        n = -n
        negative = True
    val = math.isqrt(n)
    if n == 0:
        print('3\n+ 3\n+ 4\n- 5')
    elif val ** 2 == n:
        print(1)
        if negative:
            print('-', val)
        else:
            print('+', val)
    elif n % 2:
        a, b = n // 2, n // 2 + 1
        print(2)
        if negative:
            print('-', b)
            print('+', a)
        else:
            print('+', b)
            print('-', a)
    elif n % 4 == 0:
        x = n // 4
        print(2)
        if negative:
            print('-', x + 1)
            print('+', x - 1)
        else:
            print('+', x + 1)
            print('-', x - 1)
    else:
        if n == 2:
            if negative:
                print('3\n- 6\n+ 5\n+ 3')
            else:
                print('3\n+ 6\n- 5\n- 3')
        else:
            val = math.isqrt(n)
            for i in range(1, val + 1):
                temp = n - i ** 2
                val2 = math.isqrt(temp)
                if val2 ** 2 == temp:
                    print(2)
                    if negative:
                        print('-', val2)
                        print('-', i)
                    else:
                        print('+', val2)
                        print('+', i)
                    return
            a, b = n // 2, n // 2 + 1
            print(3)
            if negative:
                print('+ 1')
                print('-', b)
                print('+', a)
            else:
                print('- 1')
                print('+', b)
                print('-', a)
    return

if __name__ == "__main__":
    main()
