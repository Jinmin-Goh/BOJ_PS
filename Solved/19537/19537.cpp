// Problem No.: 19537
// Solver:      Jinmin Goh
// Date:        20200807
// URL: https://www.acmicpc.net/problem/19537

#include <cstring>
#include <iostream>
#include <cstdlib>
#include <list>
#include <array>
#include <atomic>
#include <algorithm>
#include <deque>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <valarray>
#include <vector>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
using namespace std;

int n, h, w, roughTable[501][501], unitTable[501][501], roughness[15], m, unitInfo[62501][4], k, drow[4] = {1, -1, 0, 0}, dcol[4] = {0, 0, 1, -1}, visited[501][501];

int main() {
    // parse roughTable
    scanf("%d %d %d", &n, &h, &w);
    for(int i = 0; i < h; i++) {
        for(int j = 0; j < w; j++) {
            scanf("%d", &roughTable[i][j]);
        }
    }

    // parse roughness
    for(int i = 1; i <= n; i++) {
        scanf("%d", &roughness[i]);
    }

    // unitTable initialize
    for(int i = 0; i < h; i++) {
        for(int j = 0; j < w; j++) {
            unitTable[i][j] = -1;
        }
    }

    // unit info adding
    scanf("%d", &m);
    for(int i = 1; i <= m; i++) {
        for(int j = 0; j < 4; j++) {
            scanf("%d", &unitInfo[i][j]);
        }
        // unitTable add
        unitTable[unitInfo[i][2]][unitInfo[i][3]] = unitInfo[i][1];
    }
    scanf("%d", &k);

    // query
    for(int _ = 0; _ < k; _++) {
        // parsing order
        int u, row, col;
        scanf("%d %d %d", &u, &row, &col);
        
        // 약진 불가; 다른 유닛 존재 또는 이동 불가 지점
        if(unitTable[row][col] != -1) continue;
        if(roughness[roughTable[row][col]] == -1) continue;

        // bfs
        priority_queue<tuple<int, int, int> > tempList;
        tuple<int, int, int> tempTuple = {unitInfo[u][0], unitInfo[u][2], unitInfo[u][3]}; // power, row, col
        tuple<int, int, int> initVec = tempTuple;
        tempList.push(tempTuple);

        // todo fix
        // for(int i = 0; i < h; i++) {
        //     for(int j = 0; j < w; j++) {
        //         visited[i][j] = 0;
                
        //     }
        // }
        
        bool flag = false;
        queue<pair<int, int> > changed;
        while(tempList.size()) {
            tempTuple = tempList.top();
            tempList.pop();
            
            auto [power, tempRow, tempCol] = tempTuple;

            // power overused
            if(power < 0) continue;
            // 불가능한 칸에 들어간 경우
            if(roughness[roughTable[tempRow][tempCol]] == -1) continue;
            // reached order
            if(tempRow == row && tempCol == col) {
                flag = true;
                break;
            }
            // 적대 세력 유저가 있는 경우
            if(unitTable[tempRow][tempCol] != -1 && unitTable[tempRow][tempCol] != unitInfo[u][1]) {
                continue;
            }
            // 교전 체크
            bool fightFlag = false;
            for(int i = 0; i < 4; i++) {
                if(tempRow + drow[i] >= 0 && tempRow + drow[i] < h && tempCol + dcol[i] >= 0 && tempCol + dcol[i] < w && unitTable[tempRow + drow[i]][tempCol + dcol[i]] != -1 && unitTable[tempRow + drow[i]][tempCol + dcol[i]] != unitInfo[u][1]) {
                    // 교전에서 탈출하는 경우
                    if(tempTuple == initVec) continue;
                    fightFlag = true;
                    break;
                }
            }
            if(fightFlag) continue;
            // bfs visited
            if(visited[tempRow][tempCol]) continue;
            visited[tempRow][tempCol] = 1;
            changed.push(make_pair(tempRow, tempCol));
            //printf("%d %d %d %d\n", _, tempRow, tempCol, power);
            // queue adding
            for(int i = 0; i < 4; i++) {
                if(tempRow + drow[i] >= 0 && tempRow + drow[i] < h && tempCol + dcol[i] >= 0 && tempCol + dcol[i] < w && !visited[tempRow + drow[i]][tempCol + dcol[i]]) {
                    tuple<int, int, int> temptempVec = {power - roughness[roughTable[tempRow + drow[i]][tempCol + dcol[i]]], tempRow + drow[i], tempCol + dcol[i]};
                    tempList.push(temptempVec);
                }
            }
        }
        
        while(changed.size()) {
            int x = changed.front().first, y = changed.front().second;
            changed.pop();
            visited[x][y] = 0;
        }

        if(flag) {
            // update unitInfo & unitTable
            unitTable[unitInfo[u][2]][unitInfo[u][3]] = -1;
            unitInfo[u][2] = row;
            unitInfo[u][3] = col;
            unitTable[unitInfo[u][2]][unitInfo[u][3]] = unitInfo[u][1];
        }
    }


    for(int i = 1; i <= m; i++) {
        printf("%d %d\n", unitInfo[i][2], unitInfo[i][3]);
    }

    return 0;
}