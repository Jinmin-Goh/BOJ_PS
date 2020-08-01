// Problem No.: 14931
// Solver:      Jinmin Goh
// Date:        20200731
// URL: https://www.acmicpc.net/problem/14931

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
    int n, nums[1000010] = {};
    pair<long long int, long long int> ans;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        scanf("%d", &nums[i]);
    }

    for(int i = 0; i < n; i++) {
        int cnt = i + 1;
        long long int tempAns = 0;
        while(cnt <= n) {
            tempAns += nums[cnt - 1];
            cnt += i + 1;
        }
        if(tempAns > ans.first) {
            ans.first = tempAns;
            ans.second = i + 1;
        }
    }
    if(ans.first == 0) {
        printf("%d %d", 0, 0);
    }
    else {
        printf("%lld %lld", ans.second, ans.first);
    }



    return 0;
}