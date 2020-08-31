// Problem No.: 9998
// Solver:      Jinmin Goh
// Date:        20200831
// URL: https://www.acmicpc.net/problem/9998

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

long long AList[300010], BList[300010];

int main() {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        scanf("%lld", &AList[i]);
    }
    for(int i = 0; i < n; i++) {
        scanf("%lld", &BList[i]);
    }

    long long minVal = 1e18, lo = 0, hi = 1e12;
    while(lo < hi) {
        long long mid1 = (2 * lo + hi) / 3, mid2 = (lo + 2 * hi) / 3;
        long long mid1Val = 0, mid2Val = 0;
        for(int i = 0; i < n / 2; i++) {
            mid1Val += abs((mid1 + n / 2 - i) - AList[i]) + abs((mid1 + n / 2 - i) - BList[i]);
            mid2Val += abs((mid2 + n / 2 - i) - AList[i]) + abs((mid2 + n / 2 - i) - BList[i]);
        }
        mid1Val += abs(mid1 - AList[n / 2]) + abs(mid1 - BList[n / 2]);
        mid2Val += abs(mid2 - AList[n / 2]) + abs(mid2 - BList[n / 2]);
        for(int i = 0; i < n / 2; i++) {
            mid1Val += abs((mid1 + n / 2 - i) - AList[n - 1 - i]) + abs((mid1 + n / 2 - i) - BList[n - 1 - i]);
            mid2Val += abs((mid2 + n / 2 - i) - AList[n - 1 - i]) + abs((mid2 + n / 2 - i) - BList[n - 1 - i]);
        }

        if(mid1Val > mid2Val) {
            lo = mid1 + 1;
            minVal = min(minVal, mid2Val);
        }
        else {
            hi = mid2;
            minVal = min(minVal, mid1Val);
        }
    }

    printf("%lld", minVal);

    return 0;
}