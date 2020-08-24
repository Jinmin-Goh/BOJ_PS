// Problem No.: 18877
// Solver:      Jinmin Goh
// Date:        20200820
// URL: https://www.acmicpc.net/problem/18877

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

vector<pair<long long, long long>> interval;

int main() {
    long long n, m;
    scanf("%lld %lld", &n, &m);
    for(int i = 0; i < m; i++) {
        long long a, b;
        scanf("%lld %lld", &a, &b);
        interval.push_back(make_pair(a, b));
    }

    sort(interval.begin(), interval.end());
    long long lo = 0, hi = 1e18 + 1;

    while(lo < hi) {
        long long mid = (lo + hi + 1) / 2;
        long long prev = -1e18 - 1;
        int cnt = 0;
        for (auto& i : interval) {
            while (max(prev + mid, i.first) <= i.second) {
                prev = max(prev + mid, i.first);
                cnt++;
                if (cnt >= n) break;
            }
            if (cnt >= n) break;
        }

        if(cnt >= n) {
            lo = mid;
        }
        else {
            hi = mid - 1;
        }
    }
    printf("%lld", lo);
    return 0;
}