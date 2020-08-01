// Problem No.: 1557
// Solver:      Jinmin Goh
// Date:        20200731
// URL: https://www.acmicpc.net/problem/1557

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

long long int mobiusList[1000100];

long long int countNonSquare(long long int N) { 
    long long int ans = 0; 
    for (long long int i = 1; i * i <= N; i++) {
        ans += mobiusList[i] * (N / (i * i));
    }
    return ans;
} 

int32_t main() {
    // constructing mobius function
    for (long long int i = 1; i <= 1000000; i++) 
        mobiusList[i] = 1; 
    for (long long int i = 2; i * i <= 1000000; i++) {
        if (mobiusList[i] == 1) { 
            for (long long int j = i; j <= 1000000; j += i) {
                mobiusList[j] *= -i;
            }
            for (long long int j = i * i; j <= 1000000; j += i * i) {
                mobiusList[j] = 0;
            }
        } 
    } 
    for (long long int i = 2; i <= 1000000; i++) {
        // even primes
        if (mobiusList[i] == i) {
            mobiusList[i] = 1;
        }
        // odd primes
        else if (mobiusList[i] == -i) {
            mobiusList[i] = -1;
        }
        // even primes; one prime was bigger than sqrt(1e6)
        else if (mobiusList[i] < 0) {
            mobiusList[i] = 1;
        }
        // odd primes; one prime was bigger than sqrt(1e6)
        else if (mobiusList[i] > 0) {
            mobiusList[i] = -1;
        }
    }

    // parsing
    long long int k; 
    scanf("%lld", &k);
    
    // binary search
    long long int minVal = 0, maxVal = 1e12; 
    while (minVal + 1 < maxVal) { 
        long long int mid = (minVal + maxVal) / 2; 
        if (countNonSquare(mid) < k) minVal = mid; else maxVal = mid;
    } 
    printf("%lld", maxVal);
}
