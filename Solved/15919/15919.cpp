// Problem No.: 15919
// Solver:      Jinmin Goh
// Date:        20201014
// URL: https://www.acmicpc.net/problem/15919

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

int dpList[1010];
vector<pair<int, int> > dates(1010);

int main() {
    int n, m;
    scanf("%d", &n);
    scanf("%d", &m);
    for(int i = 0; i < m; i++) {
        scanf("%d %d", &dates[i].first, &dates[i].second);
    }
    dpList[0] = 0;
    for(int i = 1; i <= n; i++) {
        dpList[i] = 1010;
    }
    for(int i = 0; i <= n; i++) {
        for(int j = 0; j < m; j++) {
            if(dates[j].first <= i) continue;
            dpList[dates[j].second] = min(dpList[dates[j].second], max(dpList[i], dates[j].first - i - 1));
        }
    }
    int ans = 1010;
    for(int i = 0; i <= n; i++) {
        ans = min(ans, max(dpList[i], n - i));
    }
    printf("%d", ans);
    return 0;
}