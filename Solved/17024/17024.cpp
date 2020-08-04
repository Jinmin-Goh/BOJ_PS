// Problem No.: 17024
// Solver:      Jinmin Goh
// Date:        20200803
// URL: https://www.acmicpc.net/problem/17024

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

int main() {
    int n, deg[100010] = {};
    scanf("%d", &n);
    for(int i = 1; i < n; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        deg[a]++;
        deg[b]++;
    }
    int ans = 0;
    for(int i = 1; i <= n; i++) {
        ans = max(ans, deg[i]);
    }
    printf("%d", ans + 1);
    
    return 0;
}