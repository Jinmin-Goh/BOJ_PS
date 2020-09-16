// Problem No.: 19845
// Solver:      Jinmin Goh
// Date:        20200914
// URL: https://www.acmicpc.net/problem/19845

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

long long width[250010];

int main() {
    long long n, q;
    scanf("%lld %lld", &n, &q);
    for(long long i = 1; i <= n; i++) {
        scanf("%lld", &width[i]);
    }

    for(long long i = 0; i < q; i++) {
        long long x, y;
        scanf("%lld %lld", &x, &y);
        long long ans = max(0LL, width[y] - x + 1);

        // binary search
        long long lo = 1, hi = n;
        
        while(lo < hi) {
            long long mid = (lo + hi + 1) / 2;
            if(width[mid] >= x) {
                lo = mid;
            }
            else {
                hi = mid - 1;
            }
        }
        ans += max(0LL, lo - y);

        printf("%lld\n", ans);
    }

    return 0;
}