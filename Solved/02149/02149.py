# Problem No.: 2149
# Solver:      Jinmin Goh
# Date:        20220905
# URL: https://www.acmicpc.net/problem/2149

import sys

def main():
    key = sys.stdin.readline().rstrip()
    code = sys.stdin.readline().rstrip()
    table = []
    key_list = [i for i in key]
    key_list.sort()
    key_dict = {}
    for k in key_list:
        cnt = 1
        while (k, cnt) in key_dict:
            cnt += 1
        key_dict[(k, cnt)] = []
    for i in range(len(key)):
        for j in range(len(code) // len(key)):
            key_dict[list(key_dict.keys())[i]].append(code[i * (len(code) // len(key)) + j])
    decode_list = [i for i in key]
    decode_dict = {}
    for k in decode_list:
        cnt = 1
        while (k, cnt) in decode_dict:
            cnt += 1
        decode_dict[(k, cnt)] = key_dict[(k, cnt)]
    for i in range(len(code)):
        print(decode_dict[list(decode_dict.keys())[i % len(key)]][i // len(key)], end='')
    
    return

if __name__ == "__main__":
    main()