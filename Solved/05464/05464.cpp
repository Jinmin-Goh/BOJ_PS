// Problem No.: 5464
// Solver:      Jinmin Goh
// Date:        20200804
// URL: https://www.acmicpc.net/problem/5464

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

int weight[2001], cost[101], carPos[2001];

int main() {
    int n, m, ans = 0;
    priority_queue<int, vector<int>, greater<int>> emptySpace;
    queue<int> waiting;
    scanf("%d %d", &n, &m);
    for(int i = 1; i <= n; i++) {
        scanf("%d", &cost[i]);
        emptySpace.push(i);
    }
    for(int i = 1; i <= m; i++) {
        scanf("%d", &weight[i]);
    }
    for(int i = 0; i < 2 * m; i++) {
        int q;
        scanf("%d", &q);
        if(q > 0) {
            if(emptySpace.empty()) {
                waiting.push(q);
            } else {
                carPos[q] = emptySpace.top();
                emptySpace.pop();
                ans += weight[q] * cost[carPos[q]];
            }
        }
        else {
            emptySpace.push(carPos[-q]);
            if(waiting.size() > 0) {
                q = waiting.front();
                waiting.pop();
                carPos[q] = emptySpace.top();
                emptySpace.pop();
                ans += weight[q] * cost[carPos[q]];
            }
        }
    }

    printf("%d", ans);
    return 0;
}