// Problem No.: 11060
// Solver:      Jinmin Goh
// Date:        20200826
// URL: https://www.acmicpc.net/problem/11060

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

int nums[1010], dpList[1010];

int main() {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        scanf("%d", &nums[i]);
        dpList[i] = -1;
    }

    if(n == 1) {
        printf("0");
        return 0;
    }
    dpList[0] = 0;
    for(int i = 0; i < n - 1; i++) {
        if(nums[i] == 0) {
            continue;
        }
        for(int j = 1; j <= nums[i]; j++) {
            if(dpList[i + j] == -1) {
                if(dpList[i] != -1)
                    dpList[i + j] = dpList[i] + 1;
            }
            else {
                dpList[i + j] = min(dpList[i + j], dpList[i] + 1);
            }
        }
    }
    printf("%d", dpList[n - 1]);

    return 0;
}