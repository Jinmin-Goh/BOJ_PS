// Problem No.: 9520
// Solver:      Jinmin Goh
// Date:        20200827
// URL: https://www.acmicpc.net/problem/9520

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

int dpTable[1510][1510], table[1510][1510];
int n;

int solve(int left, int right) {
    if(dpTable[left][right] == -1) {
        
        int next = max(left, right) + 1;
        if(next > n) {
            return 0;
        }
        dpTable[left][right] = min(table[next][left] + solve(next, right), table[next][right] + solve(left, next));
        // dp[left][right] = min(attach next left, attach next right)
    }

    return dpTable[left][right];
}


int main() {
    scanf("%d", &n);
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            scanf("%d", &table[i][j]);
            dpTable[i][j] = -1;
        }
    }
    int ans = solve(1, 1);
    printf("%d", ans);
    return 0;
}