# Problem No.: 19585
# Solver:      Jinmin Goh
# Date:        20220816
# URL: https://www.acmicpc.net/problem/19585

import sys

def main():
    c, n = map(int, sys.stdin.readline().split())
    container = ['']
    trie = [[]]
    end = [False]
    
    def add(w):
        pos = i = 0
        while i < len(w):
            for next in trie[pos]:
                if container[next] == w[i]:
                    pos = next
                    i += 1
                    break
            else:
                trie[pos].append(len(container))
                trie.append([])
                end.append(False)
                pos = len(container)
                container.append(w[i])
                i += 1
        end[pos] = True
    
    def find(word):
        pos = i = 0
        while i < len(word) - 1:
            for next in trie[pos]:
                if container[next] == word[i]:
                    pos = next
                    i += 1
                    if end[pos]:
                        yield i
                    break
            else:
                return
    
    for _ in range(c):
        add(sys.stdin.readline().rstrip())
    name_list = {sys.stdin.readline().rstrip() for _ in range(n)}
    q = int(sys.stdin.readline().rstrip())
    for _ in range(q):
        team = sys.stdin.readline().rstrip()
        pos_list = find(team)
        if not pos_list:
            print("No")
            continue
        for i in pos_list:
            if team[i:] in name_list:
                print("Yes")
                break
        else:
            print("No")
        

    return

if __name__ == "__main__":
    main()