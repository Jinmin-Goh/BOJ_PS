// Problem No.: 15487
// Solver:      Jinmin Goh
// Date:        20200824
// URL: https://www.acmicpc.net/problem/15487

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

int nums[1000010], leftDPList[1000010], rightDPList[1000010];

int main() {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        scanf("%d", &nums[i]);
    }

    int minVal = nums[0], maxVal = nums[n - 1], ans = -1e7;
    leftDPList[0] = -1e7;
    for(int i = 1; i < n; i++) {
        leftDPList[i] = max(leftDPList[i - 1], nums[i] - minVal);
        minVal = min(minVal, nums[i]);
    }
    rightDPList[n - 1] = -1e7;
    for(int i = n - 2; i >= 0; i--) {
        rightDPList[i] = max(rightDPList[i + 1], maxVal - nums[i]);
        maxVal = max(maxVal, nums[i]);
    }
    for(int i = 0; i < n - 1; i++) {
        ans = max(ans, leftDPList[i] + rightDPList[i + 1]);
    }
    printf("%d", ans);

    return 0;
}