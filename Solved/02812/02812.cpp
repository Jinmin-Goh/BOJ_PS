// Problem No.: 2812
// Solver:      Jinmin Goh
// Date:        20201014
// URL: https://www.acmicpc.net/problem/2812

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

char nums[500010];

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    scanf("%s", nums);
    stack<char> numStack, ans;
    numStack.push(nums[0]);
    for(int i = 1; i < n; i++) {
        while(k > 0 && numStack.size() && numStack.top() < nums[i]) {
            numStack.pop();
            k--;
        }
        numStack.push(nums[i]);
    }
    for(int i = 0; i < k; i++) {
        numStack.pop();
    }
    while(numStack.size()) {
        ans.push(numStack.top());
        numStack.pop();
    }
    while(ans.size()) {
        printf("%c", ans.top());
        ans.pop();
    }
    return 0;
}