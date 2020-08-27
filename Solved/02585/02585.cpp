// Problem No.: 2585
// Solver:      Jinmin Goh
// Date:        20200826
// URL: https://www.acmicpc.net/problem/2585

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

int dist[1010][1010], fuel;
bool visited[1010];
int n, k;

bool dfs(int cur, int depth) {
    // can reach end
    if(dist[cur][n + 1] <= fuel) {
        return true;
    }
    // exceed cnt
    if(depth > k) {
        return false;
    }
    visited[cur] = true;

    for(int i = 1; i <= n; i++) {
        if(visited[i]) {
            continue;
        }
        if(dist[cur][i] > fuel) {
            continue;
        }
        if(dfs(i, depth + 1)) {
            return true;
        }
    }
    return false;

}


int main() {
    pair<int, int> station[1010];
    scanf("%d %d", &n, &k);
    for(int i = 1; i <= n; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        station[i] = make_pair(a, b);
    }

    station[n + 1] = make_pair(10000, 10000);

    // int ans = (ceil(sqrt(2 * 10000 * 10000)) + 9) / 10;
    for(int i = 0; i <= n + 1; i++) {
        for(int j = 0; j <= n + 1; j++) {
            dist[i][j] = pow(station[i].first - station[j].first, 2) + pow(station[i].second - station[j].second, 2);
        }
    }

    int hi = 14143, lo = 1;
    while(lo < hi) {
        int mid = (lo + hi + 1) / 2, maxVal = 0;
        fuel = mid * mid * 100;
        for(int i = 0; i <= n + 1; i++) {
            visited[i] = 0;
        }

        if(dfs(0, 0)) {
            hi = mid - 1;
        }
        else {
            lo = mid;
        }
    }
    printf("%d", lo + 1);

    return 0;
}