// Problem No.: 17144
// Solver:      Jinmin Goh
// Date:        20200902
// URL: https://www.acmicpc.net/problem/17144

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

int table[1010][1010], dx[4] = {1, -1, 0, 0}, dy[4] = {0, 0, 1, -1};
vector<int> airPos;

int main() {
    int n, m, t;
    scanf("%d %d %d", &n, &m, &t);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            scanf("%d", &table[i][j]);
            if(table[i][j] == -1) {
                airPos.push_back(i);
            }
        }
    }

    for(int _ = 0; _ < t; _++) {
        int newTable[1010][1010];
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                newTable[i][j] = 0;
            }
        }
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(table[i][j] > 0) {
                    newTable[i][j] += table[i][j];
                    int cnt = 0;
                    for(int k = 0; k < 4; k++) {
                        if(i + dx[k] >= 0 && i + dx[k] < n && j + dy[k] >= 0 && j + dy[k] < m && table[i + dx[k]][j + dy[k]] != -1) {
                            newTable[i][j] -= table[i][j] / 5;
                            newTable[i + dx[k]][j + dy[k]] += table[i][j] / 5;
                        }
                    }
                }
            }
        }
        
        // printf("\n");
        // for(int i = 0; i < n; i++) {
        //     for(int j = 0; j < m; j++) {
        //         printf("%d ", newTable[i][j]);
        //     }
        //     printf("\n");
        // }

        for(int i = airPos[0] - 2; i >= 0; i--) {
            newTable[i + 1][0] = newTable[i][0];
        }
        for(int i = 1; i < m; i++) {
            newTable[0][i - 1] = newTable[0][i];
        }
        for(int i = 1; i <= airPos[0]; i++) {
            newTable[i - 1][m - 1] = newTable[i][m - 1];
        }
        for(int i = m - 2; i > 0; i--) {
            newTable[airPos[0]][i + 1] = newTable[airPos[0]][i];
        }
        newTable[airPos[0]][1] = 0;

        for(int i = airPos[1] + 2; i < n; i++) {
            newTable[i - 1][0] = newTable[i][0];
        }
        for(int i = 1; i < m; i++) {
            newTable[n - 1][i - 1] = newTable[n - 1][i];
        }
        for(int i = n - 2; i >= airPos[1]; i--) {
            newTable[i + 1][m - 1] = newTable[i][m - 1];
        }
        for(int i = m - 2; i > 0; i--) {
            newTable[airPos[1]][i + 1] = newTable[airPos[1]][i];
        }
        newTable[airPos[1]][1] = 0;

        

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                table[i][j] = newTable[i][j];
            }
        }
        table[airPos[0]][0] = -1;
        table[airPos[1]][0] = -1;
        // printf("\n");
        // for(int i = 0; i < n; i++) {
        //     for(int j = 0; j < m; j++) {
        //         printf("%d ", table[i][j]);
        //     }
        //     printf("\n");
        // }
    }
    int ans = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(table[i][j] > 0) {
                ans += table[i][j];
            }
        }
    }
    printf("%d", ans);

    return 0;
}