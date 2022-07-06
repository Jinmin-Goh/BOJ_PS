# Problem No.: 25317
# Solver:      Jinmin Goh
# Date:        20220705
# URL: https://www.acmicpc.net/problem/25317

import sys

def main():
    n = int(input())
    zero_set = set()
    plus = True
    zero = False
    query = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    # coordinate compression
    nums = []
    for q in query:
        if q[0] == 1:
            a, b = q[1], q[2]
            if a != 0:
                nums.append((-b // a, (a, b)))
        elif q[0] == 2:
            nums.append((q[1], (1, -q[1])))
    nums.sort()
    n = len(nums)
    d = 0
    while 2 ** d < n:
        d += 1
    arr = [0 for _ in range(2 ** (d + 1) + 1)]
    nums_pos = {nums[i][1]:i + 1 for i in range(n)}
    for q in query:
        if q[0] == 1:   
            a, b = q[1], q[2]
            if a == 0 and b == 0:
                zero = True
                continue
            elif a == 0:
                if b < 0:
                    plus = not plus
                continue
            if a < 0:
                plus = not plus
            if b % a == 0:
                zero_set.add(-b // a)
            pos = 2 ** d + nums_pos[(a, b)] - 1
            while pos:
                arr[pos] += 1
                pos //= 2
        elif q[0] == 2:
            if zero:
                print(0)
                continue
            if q[1] in zero_set:
                print(0)
            else:
                stack = [(1, 1, 2 ** d)]
                ql = nums_pos[(1, -q[1])]
                qr = n
                val = 0
                while stack:
                    node, l, r = stack.pop()
                    if ql <= l and r <= qr:
                        val += arr[node]
                        continue
                    elif qr < l or r < ql:
                        continue
                    m = (l + r) // 2
                    stack.append((node * 2, l, m))
                    stack.append((node * 2 + 1, m + 1, r))

                if not plus:
                    val += 1
                if val % 2:
                    print('-')
                else:
                    print('+')
    return

if __name__ == "__main__":
    main()