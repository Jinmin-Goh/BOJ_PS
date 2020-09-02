// Problem No.: 2638
// Solver:      Jinmin Goh
// Date:        20200902
// URL: https://www.acmicpc.net/problem/2638

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

int dx[4] = {1, -1, 0, 0}, dy[4] = {0, 0, 1, -1};
int table[110][110];

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            scanf("%d", &table[i][j]);
        }
    }

    bool flag = true;
    int ans = 0;
    while(flag) {
        flag = false;
        int newTable[110][110];
        // initialize
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                newTable[i][j] = 0;
            }
        }


        // check outside air
        vector<pair<int, int>> checkList;
        checkList.push_back(make_pair(0, 0));
        while(checkList.size()) {
            int x = checkList.back().first, y = checkList.back().second;
            checkList.pop_back();
            if(table[x][y] == 1 || table[x][y] == 2) {
                continue;
            }
            table[x][y] = 2;
            for(int i = 0; i < 4; i++) {
                if(x + dx[i] >= 0 && x + dx[i] < n && y + dy[i] >= 0 && y + dy[i] < m) {
                    checkList.push_back(make_pair(x + dx[i], y + dy[i]));
                }
            }
        }
        

        // find 1 and check melting
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(table[i][j] == 1) {
                    flag = true;
                    int cnt = 0;
                    for(int p = 0; p < 4; p++) {
                        if(table[i + dx[p]][j + dy[p]] == 2) {
                            cnt++;
                        }
                    }
                    if(cnt <= 1) {
                        newTable[i][j] = 1;
                    }
                }
            }
        }
        //printf("\n");
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                table[i][j] = newTable[i][j];
                //printf("%d ", table[i][j]);
            }
            //printf("\n");
        }
        if(!flag) break;
        ans++;
    }

    printf("%d", ans);
    return 0;
}