// Problem No.: 
// Solver:      Jinmin Goh
// Date:        20200726
// URL: https://www.acmicpc.net/problem/

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

int main() {
    int n, m, cows[100010], a[100010], b[100010], w[100010];
    vector<vector<int>> edge;
    bool flag = true;
    // parsing
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++) {
        scanf("%d", &cows[i]);
        if(cows[i] != i + 1) {
            flag = false;
        }
    }
    for(int i = 0; i < m; i++) {
        scanf("%d %d %d", &a[i], &b[i], &w[i]);
        edge.push_back(vector<int> {w[i], a[i], b[i]});
    }
    sort(edge.begin(), edge.end());

    // no need to change
    if(flag) {
        printf("%d", -1);
        return 0;
    }

    // do binary search for answer
    int left = 0, right = m - 1;
    while(left < right) {
        int mid = (left + right + 1) / 2;
        bool connectFlag = true;

        // do union(for connected components) - find(check whether all different components are connected)

        if(connectFlag) {
            left = mid + 1;
        }
        else {
            right = mid;
        }
    }
    
    return 0;
}