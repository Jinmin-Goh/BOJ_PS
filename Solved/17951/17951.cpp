// Problem No.: 17951
// Solver:      Jinmin Goh
// Date:        20200910
// URL: https://www.acmicpc.net/problem/17951

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

int nums[100010];

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    for(int i = 0; i < n; i++) {
        scanf("%d", &nums[i]);
    }
    int lo = 0, hi = 1e9;
    while(lo < hi) {
        int mid = (lo + hi + 1) / 2, sumVal = 0, cnt = 0;
        for(int i = 0; i < n; i++) {
            sumVal += nums[i];
            if(sumVal >= mid) {
                sumVal = 0;
                cnt++;
            }
        }
        if(cnt >= k) {
            lo = mid;
        }
        else{
            hi = mid - 1;
        }
    }
    printf("%d", lo);
    return 0;
}