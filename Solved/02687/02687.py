# Problem No.: 2687
# Solver:      Jinmin Goh
# Date:        20220905
# URL: https://www.acmicpc.net/problem/2687

import sys

def main():
    t = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n = int(sys.stdin.readline().rstrip())
        code = []
        for _ in range((2 * n - 1) // 80 + 1):
            temp = sys.stdin.readline().rstrip()
            code.append(temp)
        code = ''.join(code)
        p = 0
        decode = []
        while p < 2 * n:
            head = int(code[p:p + 2], 16)
            p += 2
            if head & 0x80:
                head &= 0x7F
                head += 3
                decode.append(code[p:p + 2] * head)
                p += 2
            else:
                decode.append(code[p:p + (head + 1) * 2])
                p += (head + 1) * 2
        ans = ''.join(decode)
        print(len(ans) // 2)
        cnt = 0
        while cnt < len(ans):
            print(ans[cnt:min(cnt + 80, len(ans))])
            cnt += 80
    return

if __name__ == "__main__":
    main()