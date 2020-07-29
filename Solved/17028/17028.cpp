// Problem No.: 17028
// Solver:      Jinmin Goh
// Date:        20200729
// URL: https://www.acmicpc.net/problem/17028

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

int nums[110];

bool check(int n) {
    bool flag = true;
    for(int i = 1; i <= n; i++) {
        if(i != nums[i]) {
            flag = false;
            break;
        }
    }
    return flag;
}

int main() {
    int n;
    scanf("%d", &n);
    for(int i = 1; i <= n; i++) {
        scanf("%d", &nums[i]);
    }

    if(check(n)) {
        printf("0");
        return 0;
    }
    int revPos;
    for(int i = 1; i < n; i++) {
        if(nums[i] > nums[i + 1]) {
            revPos = i;
        }
    }
    printf("%d", revPos);

    return 0;
}