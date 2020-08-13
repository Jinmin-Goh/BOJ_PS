// Problem No.: 15898
// Solver:      Jinmin Goh
// Date:        20200812
// URL: https://www.acmicpc.net/problem/15898

#include <cassert>
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

int n, dx[4] = {0, 1, 0, 1}, dy[4] = {0, 0, 1, 1}, ans = 0;
bool usingList[10];
int ingVal[10][4][4][4];    // number, rotate status, row, col
char ingCol[10][4][4][4];   // number, rotate status, row, col

// rotate 90 deg cw
void rotateFunc(int cnt, int rot) {
    ingVal[cnt][rot][1][2] = ingVal[cnt][rot - 1][1][1];
    ingVal[cnt][rot][2][2] = ingVal[cnt][rot - 1][1][2];
    ingVal[cnt][rot][2][1] = ingVal[cnt][rot - 1][2][2];
    ingVal[cnt][rot][1][1] = ingVal[cnt][rot - 1][2][1];
    for(int i = 0; i < 3; i++) {
        ingVal[cnt][rot][i][3] = ingVal[cnt][rot - 1][0][i];
        ingVal[cnt][rot][3][3 - i] = ingVal[cnt][rot - 1][i][3];
        ingVal[cnt][rot][3 - i][0] = ingVal[cnt][rot - 1][3][3 - i];
        ingVal[cnt][rot][0][i] = ingVal[cnt][rot - 1][3 - i][0];
    }

    ingCol[cnt][rot][1][2] = ingCol[cnt][rot - 1][1][1];
    ingCol[cnt][rot][2][2] = ingCol[cnt][rot - 1][1][2];
    ingCol[cnt][rot][2][1] = ingCol[cnt][rot - 1][2][2];
    ingCol[cnt][rot][1][1] = ingCol[cnt][rot - 1][2][1];
    for(int i = 0; i < 3; i++) {
        ingCol[cnt][rot][i][3] = ingCol[cnt][rot - 1][0][i];
        ingCol[cnt][rot][3][3 - i] = ingCol[cnt][rot - 1][i][3];
        ingCol[cnt][rot][3 - i][0] = ingCol[cnt][rot - 1][3][3 - i];
        ingCol[cnt][rot][0][i] = ingCol[cnt][rot - 1][3 - i][0];
    }
}

void makingFunc(int stage, int tableVal[5][5], char tableCol[5][5]) {
    if(stage == 3) {
        int value = 0;
        for(int i = 0; i < 5; i++) {
            for(int j = 0; j < 5; j++){
                if(tableCol[i][j] == 'R') {
                    value += 7 * tableVal[i][j];
                }
                else if(tableCol[i][j] == 'B') {
                    value += 5 * tableVal[i][j];
                }
                else if(tableCol[i][j] == 'G') {
                    value += 3 * tableVal[i][j];
                }
                else if(tableCol[i][j] == 'Y') {
                    value += 2 * tableVal[i][j];
                }
            }
        }
        //printf("%d ", value);
        ans = max(ans, value);
        return;
    }

    for(int i = 0; i < n; i++) {
        if(usingList[i]) {
            continue;
        }
        usingList[i] = true;
        // for changed status
        
        
        for(int pos = 0; pos < 4; pos++) {
            for(int rot = 0; rot < 4; rot++) {
                int tempTableVal[5][5];
                char tempTableCol[5][5];
                for(int p = 0; p < 5; p++) {
                    for(int q = 0; q < 5; q++) {
                        tempTableVal[p][q] = tableVal[p][q];
                        tempTableCol[p][q] = tableCol[p][q];
                    }
                }
                
                for(int p = 0; p < 4; p++) {
                    for(int q = 0; q < 4; q++) {
                        tempTableVal[p + dx[pos]][q + dy[pos]] = tableVal[p + dx[pos]][q + dy[pos]] + ingVal[i][rot][p][q];
                        tempTableVal[p + dx[pos]][q + dy[pos]] = max(0, tempTableVal[p + dx[pos]][q + dy[pos]]);
                        tempTableVal[p + dx[pos]][q + dy[pos]] = min(9, tempTableVal[p + dx[pos]][q + dy[pos]]);

                        if(ingCol[i][rot][p][q] != 'W') {
                            tempTableCol[p + dx[pos]][q + dy[pos]] = ingCol[i][rot][p][q];
                        }
                    }
                }
                
                makingFunc(stage + 1, tempTableVal, tempTableCol);
            }
        }
        usingList[i] = false;
    }
}

int main() {
    int tableVal[5][5];
    char tableCol[5][5];

    scanf("%d", &n);
    for(int _ = 0; _ < n; _++) {
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                scanf("%d", &ingVal[_][0][i][j]);
            }
        }
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                cin >> ingCol[_][0][i][j];
            }
        }
        for(int i = 1; i < 4; i++) {
            rotateFunc(_, i);
        }
    }

    // initialization
    for(int i = 0; i < 5; i++) {
        for(int j = 0; j < 5; j++) {
            tableVal[i][j] = 0;
            tableCol[i][j] = 0;
        }
    }
    makingFunc(0, tableVal, tableCol);

    printf("%d", ans);
    return 0;
}