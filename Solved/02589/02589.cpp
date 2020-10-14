// Problem No.: 2589
// Solver:      Jinmin Goh
// Date:        20201014
// URL: https://www.acmicpc.net/problem/2589

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


int visited[50][50], dx[4] = {1, -1, 0, 0}, dy[4] = {0, 0, 1, -1};
char table[55][55];

int main() {
    int n, m;
    scanf("%d %d\n", &n, &m);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            scanf("%c", &table[i][j]);
        }
        if(i != n - 1)
            scanf("\n");
    }
    int ans = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(table[i][j] == 'L') {
                for(int p = 0; p < n; p++) {
                    for(int q = 0; q < m; q++) {
                        visited[p][q] = 0;
                    }
                }
                queue<pair<int, int>> queueList;
                queueList.push(make_pair(i, j));
                int cnt = 0;
                while(queueList.size()) {
                    queueList.push(make_pair(-1, -1));
                    while(1) {
                        pair<int, int> temp = queueList.front();
                        queueList.pop();
                        if(temp.first == -1 && temp.second == -1) {
                            break;
                        }
                        int x = temp.first, y = temp.second;
                        if(visited[x][y] || table[x][y] == 'W') continue;
                        visited[x][y] = 1;
                        for(int t = 0; t < 4; t++) {
                            if(0 <= x + dx[t] && n > x + dx[t] && 0 <= y + dy[t] && m > y + dy[t]) {
                                queueList.push(make_pair(x + dx[t], y + dy[t]));
                            }
                        }

                    }
                    cnt++;
                }
                ans = max(ans, cnt);
            }
        }
    }
    printf("%d", ans - 2);
    return 0;
}