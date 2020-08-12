// Problem No.: 11659
// Solver:      Jinmin Goh
// Date:        20200812
// URL: https://www.acmicpc.net/problem/11659

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

int nums[100010];

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++) {
        if(i == 0) {
            scanf("%d", &nums[i]);
        }
        else {
            int temp;
            scanf("%d", &temp);
            nums[i] = nums[i - 1] + temp;
        }
    }
    for(int i = 0; i < m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        if(a == 1) {
            printf("%d\n", nums[b - 1]);
        }
        else {
            printf("%d\n", nums[b - 1] - nums[a - 2]);
        }
    }
    return 0;
}