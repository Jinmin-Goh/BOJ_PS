// Problem No.: 18320
// Solver:      Jinmin Goh
// Date:        20200721
// URL: https://www.acmicpc.net/problem/18320

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

// solution: http://www.usaco.org/current/data/sol_loan_silver_jan20.html

int check(long long int n, long long int k, long long int m, long long int midVal) {
    long long int given = 0;
    long long int cnt = 0;
    while(given < n && k - cnt > 0) {
        long long int y = (n - given) / midVal;
        if(y < m) {
            return ((n - given + m - 1) / m) <= (k - cnt);
        }
        long long int maxMatch = n - midVal * y;
        long long int sameDays = (maxMatch - given) / y + 1;
        if(sameDays > k - cnt) {
            sameDays = k - cnt;
        }
        given += y * sameDays;
        cnt += sameDays;
    }
    return given >= n;
}

int main() {
    long long int n, k, m;
    scanf("%lld %lld %lld", &n, &k, &m);
    // binary search, complexity analysis
    long long int midVal = 0;
    long long int minVal = 1, maxVal = 1e12;
    while(minVal < maxVal) {
        midVal = (minVal + maxVal + 1) / 2;
        bool flag = check(n, k, m, midVal);
        if(!flag) {
            maxVal = midVal - 1;
        }
        else {
            minVal = midVal;
        }

    }
    
    printf("%lld", minVal);
    
    return 0;
}