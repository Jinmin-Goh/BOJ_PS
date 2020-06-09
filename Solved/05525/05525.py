# Problem No.: 5525
# Solver:      Jinmin Goh
# Date:        20200608
# URL: https://www.acmicpc.net/problem/5525

# AC, O(n) solution

import sys

def main():
    n = int(input())
    m = int(input())
    s = sys.stdin.readline().strip()
    #stack = [_ for _ in s]
    temp = "I" + "OI" * n
    ans = 0
    cnt = 0
    pointer = 0
    flag = False
    oflag = False
    while pointer < m:
        #print(pointer, ans)
        if flag:
            if oflag:
                if s[pointer] == "O":
                    pointer += 1
                    oflag = not oflag
                else:
                    flag = False
                    oflag = False
                    
            else:
                if s[pointer] == "I":
                    ans += 1
                    pointer += 1
                    oflag = not oflag
                else:
                    flag = False
        else:
            cnt = 0
            while pointer < m and cnt <= 2 * n and temp[cnt] == s[pointer]:
                cnt += 1
                pointer += 1
            if cnt > 2 * n:
                flag = True
                pointer -= 1
            else:
                if pointer < m and s[pointer] == "O":
                    pointer += 1
    
    print(ans)
    return

if __name__ == "__main__":
    main()