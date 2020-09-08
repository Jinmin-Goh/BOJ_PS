// Problem No.: 2293
// Solver:      Jinmin Goh
// Date:        20200904
// URL: https://www.acmicpc.net/problem/2293

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

int dpList[10010], coin[110];

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    for(int i = 0; i < n; i++) {
        scanf("%d", &coin[i]);
    }

    sort(coin, coin + n);

    dpList[0] = 1;
    for(int i = 0; i < n; i++) {
        for(int j = 1; j <= k; j++) {
            if(j >= coin[i]) {
                dpList[j] = dpList[j] + dpList[j - coin[i]];
            }
        }
    }

    printf("%d", dpList[k]);

    return 0;
}