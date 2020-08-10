// Problem No.: 19539
// Solver:      Jinmin Goh
// Date:        20200807
// URL: https://www.acmicpc.net/problem/19539

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

int n, nums[100010];

int main() {
    scanf("%d", &n);
    int sumVal = 0, oddCnt = 0, evenCnt = 0;
    for(int i = 0; i < n; i++) {
        scanf("%d", &nums[i]);
        sumVal += nums[i];
        if(nums[i] % 2) {
            oddCnt++;
        }
        else {
            evenCnt++;
        }
    }

    if(sumVal % 3 || (sumVal - oddCnt) / 2 < oddCnt) {
        printf("NO");
        return 0;
    }
    
    printf("YES");
    return 0;
}