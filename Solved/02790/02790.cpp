// Problem No.: 5821
// Solver:      Jinmin Goh
// Date:        20200824
// URL: https://www.acmicpc.net/problem/5821

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

int nums[300010];

int main() {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        scanf("%d", &nums[i]);
    }

    sort(nums, nums + n);
    int maxVal = 0;
    for(int i = 0; i < n; i++) {
        nums[i] += n - i;
        maxVal = max(maxVal, nums[i]);
    }
    int p = 0;
    while(nums[p]< maxVal) {
        p++;
        nums[p] += p;
    }
    printf("%d", n - p);

    return 0;
}