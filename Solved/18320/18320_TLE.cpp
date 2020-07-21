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

int main() {
    long long int n, k, m;
    scanf("%lld %lld %lld", &n, &k, &m);
    // binary search?
    long long int midVal = 0;
    long long int minVal = 1, maxVal = 1e12;
    while(minVal < maxVal) {
        midVal = (minVal + maxVal + 1) / 2;
        long long int given = 0;
        long long int cnt = 0;
        bool flag = true;
        // this part TLE
        while(given < n && k - cnt > 0) {
            long long int y = (n - given) / midVal;
            if(y < m) {
                if((n - given + m - 1) / m <= k - cnt) {
                    flag = true;
                    break;
                }
                else {
                    flag = false;
                    break;
                }
            }
            given += y;
            cnt += 1;

        }
        if(!flag || given >= n) {
            maxVal = midVal - 1;
        }
        else {
            minVal = midVal;
        }

    }
    
    printf("%lld", minVal);
    
    return 0;
}