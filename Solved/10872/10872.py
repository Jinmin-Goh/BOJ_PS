# Problem No.: 10872
# Solver:      Jinmin Goh
# Date:        20220718
# URL: https://www.acmicpc.net/problem/10872

import sys

def main():
    ans = [1]
    for i in range(12):
        ans.append(ans[-1] * (i + 1))
    print(ans[int(input())])
    return

if __name__ == "__main__":
    main()