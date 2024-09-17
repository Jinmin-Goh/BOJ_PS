# Problem No.: 25624
# Solver:      Jinmin Goh
# Date:        20220919
# URL: https://www.acmicpc.net/problem/25624

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    words = [[] for _ in range(n)]
    words_set = set()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for _ in range(m):
        temp = sys.stdin.readline().rstrip()
        if temp in words_set:
            print("NO")
            return
        words_set.add(temp)
        for i in range(n):
            words[i].append(temp[i])
    for i in range(n):
        words[i] = list(set(words[i]))
        words[i].sort()
    for s in alphabet:
        flag = False
        for i in range(n):
            if s in words[i]:
                if flag:
                    print("NO")
                    return
                flag = True
    val = 1
    for w in words:
        val *= len(w)
    if val == len(words_set):
        print("YES")
        for i in range(n):
            print(''.join(words[i]))
    else:
        print("NO")
    return

if __name__ == "__main__":
    main()