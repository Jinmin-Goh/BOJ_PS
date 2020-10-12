// Problem No.: 11567
// Solver:      Jinmin Goh
// Date:        20201012
// URL: https://www.acmicpc.net/problem/11567

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

int n, m, r1, c1, r2, c2, dc[4] = {1, -1, 0, 0}, dr[4] = {0, 0, 1, -1};
char table[510][510];

int main() {
    scanf("%d %d\n", &n, &m);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            scanf("%c", &table[i][j]);
        }
        scanf("\n");
    }
    scanf("%d %d", &r1, &c1);
    scanf("%d %d", &r2, &c2);

    queue<pair<int, int> > queueList;
    queueList.push(make_pair(r1, c1));
    while (queueList.size()) {
        pair<int, int> temp = queueList.front();
        queueList.pop();
        int r = temp.first, c = temp.second;
        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i], nc = c + dc[i];
            if (!(0 < r + dr[i] && n >= r + dr[i] && 0 < c + dc[i] && m >= c + dc[i])) {
                continue;
            }
            if(nr == r2 && nc == c2) {
                if(table[nr][nc] == '.') {
                    table[nr][nc] = 'X';
                    queueList.push(make_pair(nr, nc));
                }
                else {
                    printf("YES");
                    return 0;
                }
            }
            else if(table[nr][nc] == '.') {
                table[nr][nc] = 'X';
                queueList.push(make_pair(nr, nc));
            }
        }
    }
    printf("NO");
    return 0;
}