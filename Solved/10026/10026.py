# Problem No.: 10026
# Solver:      Jinmin Goh
# Date:        20200618
# URL: https://www.acmicpc.net/problem/10026

import sys

def main():
    n = int(input())
    graph = []
    graphDis = []
    for _ in range(n):
        temp = sys.stdin.readline().strip()
        tempList = [i for i in temp]
        graph.append(tempList)
        graphDis.append(tempList[:])
    
    # normal person
    ans1 = 0
    Rcnt = 0
    Gcnt = 0
    Bcnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == ".":
                continue
            ans1 += 1
            if graph[i][j] == "R":
                stack = [[i, j]]
                while stack:
                    temp = stack.pop()
                    x = temp[0]
                    y = temp[1]
                    if graph[x][y] != "R":
                        continue
                    graph[x][y] = "."
                    if x > 0:
                        stack.append([x - 1, y])
                    if x < n - 1:
                        stack.append([x + 1, y])
                    if y > 0:
                        stack.append([x, y - 1])
                    if y < n - 1:
                        stack.append([x, y + 1])
            elif graph[i][j] == "G":
                stack = [[i, j]]
                while stack:
                    temp = stack.pop()
                    x = temp[0]
                    y = temp[1]
                    if graph[x][y] != "G":
                        continue
                    graph[x][y] = "."
                    if x > 0:
                        stack.append([x - 1, y])
                    if x < n - 1:
                        stack.append([x + 1, y])
                    if y > 0:
                        stack.append([x, y - 1])
                    if y < n - 1:
                        stack.append([x, y + 1])
            else:
                stack = [[i, j]]
                while stack:
                    #print(stack, graph)
                    temp = stack.pop()
                    x = temp[0]
                    y = temp[1]
                    if graph[x][y] != "B":
                        continue
                    graph[x][y] = "."
                    if x > 0:
                        stack.append([x - 1, y])
                    if x < n - 1:
                        stack.append([x + 1, y])
                    if y > 0:
                        stack.append([x, y - 1])
                    if y < n - 1:
                        stack.append([x, y + 1])
    
    #print(graphDis)

    # abnormal person
    ans2 = 0
    Rcnt = 0
    Gcnt = 0
    Bcnt = 0
    for i in range(n):
        for j in range(n):
            if graphDis[i][j] == ".":
                continue
            ans2 += 1
            if graphDis[i][j] == "B":
                stack = [[i, j]]
                while stack:
                    temp = stack.pop()
                    x = temp[0]
                    y = temp[1]
                    if graphDis[x][y] != "B":
                        continue
                    graphDis[x][y] = "."
                    if x > 0:
                        stack.append([x - 1, y])
                    if x < n - 1:
                        stack.append([x + 1, y])
                    if y > 0:
                        stack.append([x, y - 1])
                    if y < n - 1:
                        stack.append([x, y + 1])
            else:
                stack = [[i, j]]
                while stack:
                    temp = stack.pop()
                    x = temp[0]
                    y = temp[1]
                    #print(graphDis[x][y])
                    if graphDis[x][y] != "R" and graphDis[x][y] != "G":
                        continue
                    graphDis[x][y] = "."
                    if x > 0:
                        stack.append([x - 1, y])
                    if x < n - 1:
                        stack.append([x + 1, y])
                    if y > 0:
                        stack.append([x, y - 1])
                    if y < n - 1:
                        stack.append([x, y + 1])
            #print(graphDis)
    print(ans1, ans2)
            

    return

if __name__ == "__main__":
    main()