// Problem No.: 18319
// Solver:      Jinmin Goh
// Date:        20200720
// URL: https://www.acmicpc.net/problem/18319

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
    int n, k;
    vector<int> nums;
    scanf("%d %d", &n, &k);
    for(int i = 0; i < n; i++) {
        int temp;
        scanf("%d", &temp);
        nums.push_back(temp);
    }

    sort(nums.begin(), nums.end());
    while(nums.at(nums.size() - k) < (nums.back() + 1) / 2) {
        int temp1 = nums.back() / 2, temp2 = (nums.back() + 1) / 2;
        nums.pop_back();
        nums.push_back(temp1);
        nums.push_back(temp2);
        sort(nums.begin(), nums.end());
    }
    int ans = 0;
    for(int i = 0; i < (k / 2); i++) {
        ans += nums.at(nums.size() - k + i);
    }
    printf("%d", ans);

    return 0;
}