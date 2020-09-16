// Problem No.: 19847
// Solver:      Jinmin Goh
// Date:        20200916
// URL: https://www.acmicpc.net/problem/19847

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

int nums[300010], checkList[1000010];

int main() {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        scanf("%d", &nums[i]);
    }
    int minVal = nums[0];
    for(int i = 0; i < nums[0]; i++) {
        checkList[i] = 1;
    }
    for(int i = 1; i < n; i++) {
        if(nums[i] >= minVal) continue;

        for(int j = nums[i]; j < minVal; j++) {
            checkList[j % nums[i]] += checkList[j];
        }
        minVal = nums[i];
    }
    double ans = 0;
    for(int i = 0; i < minVal; i++) {
        ans += (double) i * checkList[i];
    }
    ans /= nums[0];

    printf("%.12lf", ans);
    return 0;
}