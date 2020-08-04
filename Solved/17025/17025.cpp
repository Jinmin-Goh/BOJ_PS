// Problem No.: 17025
// Solver:      Jinmin Goh
// Date:        20200804
// URL: https://www.acmicpc.net/problem/17025

#include <algorithm>
#include <array>
#include <atomic>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <valarray>
#include <vector>
using namespace std;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int main() {
    int n, area = 0, peri = 0;
    scanf("%d", &n);
    char table[1010][1010];
    for (int i = 0; i < n; i++) {
        scanf("%s", table[i]);
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (table[i][j] != '#') {
                continue;
            }
            int tempArea = 0, tempPeri = 0;
            vector<pair<int, int>> stackList;
            stackList.push_back(pair<int, int>(i, j));

            while (stackList.size()) {
                pair<int, int> temp = stackList.back();
                stackList.pop_back();
                if (table[temp.first][temp.second] != '#') {
                    continue;
                }
                table[temp.first][temp.second] = 'X';
                tempArea++;

                for (int i = 0; i < 4; i++) {
                    if (temp.first + dx[i] >= 0 && temp.first + dx[i] < n && temp.second + dy[i] >= 0 && temp.second + dy[i] < n) {
                        if (table[temp.first + dx[i]][temp.second + dy[i]] == '.') {
                            tempPeri++;
                        }
                        stackList.push_back(pair<int, int>(temp.first + dx[i], temp.second + dy[i]));
                    } else {
                        if (!(temp.first + dx[i] >= 0 && temp.first + dx[i] < n)) {
                            tempPeri++;
                            if(temp.first + dx[i] < 0 && table[temp.first][temp.second + dy[i]] == '.') {
                                tempPeri++;
                            }
                            if(temp.first + dx[i] == n && table[temp.first][temp.second + dy[i]] == '.') {
                                tempPeri++;
                            }
                        }
                        if (!(temp.second + dy[i] >= 0 && temp.second + dy[i] < n)) {
                            tempPeri++;
                            if(temp.second + dy[i] < 0 && table[temp.first + dx[i]][temp.second] == '.') {
                                tempPeri++;
                            }
                            if(temp.second + dy[i] == n && table[temp.first + dx[i]][temp.second] == '.') {
                                tempPeri++;
                            }
                        }
                        
                    }
                }
            }
            if(tempArea > area) {
                area = tempArea;
                peri = tempPeri;
            }
            else if(tempArea == area) {
                peri = min(peri, tempPeri);
            }
        }
    }
    printf("%d %d", area, peri);
    return 0;
}