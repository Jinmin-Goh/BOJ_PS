// Problem No.: 14502
// Solver:      Jinmin Goh
// Date:        20200831
// URL: https://www.acmicpc.net/problem/14502

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

int table[8][8], visited[8][8], dx[4] = {1, -1, 0, 0}, dy[4] = {0, 0, 1, -1};
vector<pair<int, int>> zeroList, virus;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            scanf("%d", &table[i][j]);
            if(table[i][j] == 0) {
                zeroList.push_back(make_pair(i, j));
            }
            if(table[i][j] == 2) {
                virus.push_back(make_pair(i, j));
            }
        }
    }
    int ans = 0;
    for(int i = 0; i < zeroList.size() - 2; i++) {
        for(int j = i + 1; j < zeroList.size() - 1; j++) {
            for(int k = j + 1; k < zeroList.size(); k++) {
                table[zeroList[i].first][zeroList[i].second] = 1;
                table[zeroList[j].first][zeroList[j].second] = 1;
                table[zeroList[k].first][zeroList[k].second] = 1;
                
                int copyTable[8][8];
                for(int p = 0; p < n; p++) {
                    for(int q = 0; q < m; q++) {
                        copyTable[p][q] = table[p][q];
                        visited[p][q] = 0;
                    }
                }

                vector<pair<int, int>> tempList = virus;
                while(tempList.size()) {
                    pair<int, int> temp = tempList.back();
                    tempList.pop_back();
                    int x = temp.first, y = temp.second;
                    if(copyTable[x][y] == 1 || visited[x][y]) {
                        continue;
                    }
                    copyTable[x][y] = 2;
                    visited[x][y] = 1;
                    for(int t = 0; t < 4; t++) {
                        if(x + dx[t] >= 0 && x + dx[t] < n && y + dy[t] >= 0 && y + dy[t] < m) {
                            tempList.push_back(make_pair(x + dx[t], y + dy[t]));
                        }
                    }
                }
                int tempAns = 0;
                for(int p = 0; p < n; p++) {
                    for(int q = 0; q < m; q++) {
                        if(copyTable[p][q] == 0) {
                            tempAns++;
                        }
                    }
                }

                ans = max(ans, tempAns);

                table[zeroList[i].first][zeroList[i].second] = 0;
                table[zeroList[j].first][zeroList[j].second] = 0;
                table[zeroList[k].first][zeroList[k].second] = 0;
            }
        }
    }
    printf("%d", ans);
    return 0;
}