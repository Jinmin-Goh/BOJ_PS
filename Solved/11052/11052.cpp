// Problem No.: 11052
// Solver:      Jinmin Goh
// Date:        20200824
// URL: https://www.acmicpc.net/problem/11052

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

int dpList[1010], nums[1010];

int main() {
    int n;
    scanf("%d", &n);
    for(int i = 1; i <= n; i++) {
        scanf("%d", &nums[i]);
    }
    for(int i = 1; i <= n; i++) {
        dpList[i] = nums[i];
        // if(!(i % 2)) {
        //     dpList[i] = max(dpList[i], dpList[i / 2] * 2);
        // }
        for(int j = 1; j <= i / 2; j++) {
            dpList[i] = max(dpList[i], dpList[j] + dpList[i - j]);
        }
    }

    printf("%d", dpList[n]);


    return 0;
}