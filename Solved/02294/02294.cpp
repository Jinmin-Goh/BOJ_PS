// Problem No.: 2294
// Solver:      Jinmin Goh
// Date:        20200904
// URL: https://www.acmicpc.net/problem/2294

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

int dpList[100010], coin[110];

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    for(int i = 1; i <= k; i++) {
        dpList[i] = 1e9;
    }
    for(int i = 0; i < n; i++) {
        scanf("%d", &coin[i]);
        dpList[coin[i]] = 1;
    }

    sort(coin, coin + n);

    for(int i = 1; i <= k; i++) {
        for(int j = 1; j <= i / 2; j++) {
            dpList[i] = min(dpList[i], dpList[j] + dpList[i - j]);
        }
    }
    if(dpList[k] == 1e9) {
        printf("-1");
    }
    else {
        printf("%d", dpList[k]);
    }

    return 0;
}