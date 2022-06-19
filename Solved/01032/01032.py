# Problem No.: 1032
# Solver:      Jinmin Goh
# Date:        20220619
# URL: https://www.acmicpc.net/problem/1032

import sys

def main():
    n = int(input())
    query = []
    for _ in range(n):
        query.append(input())
    ans = query[0]
    for string in query:
        for i in range(len(ans)):
            if ans[i] != string[i]:
                ans = ans[:i] + '?' + ans[i + 1:]
    print(ans)
    return

if __name__ == "__main__":
    main()