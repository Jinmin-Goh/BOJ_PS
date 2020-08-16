// Problem No.: 2096
// Solver:      Jinmin Goh
// Date:        20200816
// URL: https://www.acmicpc.net/problem/2096

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

int nums[3];
int dpMaxTable[2][3], dpMinTable[2][3];

int main() {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < 3; i++) {
        scanf("%d", &nums[i]);
        dpMinTable[0][i] = nums[i];
        dpMaxTable[0][i] = nums[i];
    }

    for(int i = 0; i < n - 1 ; i++) {
        for(int j = 0; j < 3; j++) {
            scanf("%d", &nums[j]);
        }
        dpMinTable[1][0] = min(dpMinTable[0][0], dpMinTable[0][1]) + nums[0];
        dpMinTable[1][1] = min(dpMinTable[0][0], min(dpMinTable[0][1], dpMinTable[0][2])) + nums[1];
        dpMinTable[1][2] = min(dpMinTable[0][1], dpMinTable[0][2]) + nums[2];

        dpMaxTable[1][0] = max(dpMaxTable[0][0], dpMaxTable[0][1]) + nums[0];
        dpMaxTable[1][1] = max(dpMaxTable[0][0], max(dpMaxTable[0][1], dpMaxTable[0][2])) + nums[1];
        dpMaxTable[1][2] = max(dpMaxTable[0][1], dpMaxTable[0][2]) + nums[2];

        for(int j = 0; j < 3; j++) {
            dpMinTable[0][j] = dpMinTable[1][j];
            dpMaxTable[0][j] = dpMaxTable[1][j];
        }
    }
    printf("%d %d", max(dpMaxTable[0][0], max(dpMaxTable[0][1], dpMaxTable[0][2])), min(dpMinTable[0][0], min(dpMinTable[0][1], dpMinTable[0][2])));

    return 0;
}