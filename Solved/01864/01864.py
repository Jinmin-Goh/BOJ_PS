# Problem No.: 1864
# Solver:      Jinmin Goh
# Date:        20220625
# URL: https://www.acmicpc.net/problem/1864

import sys

def main():
    nums = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}
    while True:
        text = sys.stdin.readline().rstrip()
        if text == '#':
            break
        text = list(text)
        ans = 0
        cnt = 0
        while text:
            ans += nums[text.pop()] * (8 ** cnt)
            cnt += 1
        print(ans)

    return

if __name__ == "__main__":
    main()