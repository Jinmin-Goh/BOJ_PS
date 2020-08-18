// Problem No.: 15719
// Solver:      Jinmin Goh
// Date:        20200818
// URL: https://www.acmicpc.net/problem/15719

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

int main() {
    long long int n, ans = 0;
    scanf("%lld", &n);
    for(int i = 0; i < n; i++) {
        long long int temp;
        scanf("%lld", &temp);
        ans += temp;
    }
    printf("%lld", ans - n * (n - 1) / 2);
    return 0;
}