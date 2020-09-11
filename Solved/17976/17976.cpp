// Problem No.: 17976
// Solver:      Jinmin Goh
// Date:        20200910
// URL: https://www.acmicpc.net/problem/17976

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

vector<pair<long long, long long>> thread;

int main() {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        long long a, b;
        scanf("%lld %lld", &a, &b);
        thread.push_back(make_pair(a, b));
    }

    sort(thread.begin(), thread.end());

    long long lo = 0, hi = 1e9 * 2 + 10;
    while(lo < hi) {
        long long mid = (lo + hi + 1) / 2;

        long long knot[100010];
        for(int i = 0; i < n; i++) {
            knot[i] = 0;
        }
        knot[0] = thread[0].first;
        bool flag = false;
        for(int i = 0; i < n - 1; i++) {
            if(mid <= thread[i + 1].first - knot[i]) {
                knot[i + 1] = thread[i + 1].first;
            }
            else {
                if(mid + knot[i] > thread[i + 1].first + thread[i + 1].second) {
                    flag = true;
                    break;
                }
                else {
                    knot[i + 1] = knot[i] + mid;
                }
            }
        }

        if(!flag) {
            lo = mid;
        }
        else {
            hi = mid - 1;
        }
    }
    printf("%lld", lo);
    return 0;
}