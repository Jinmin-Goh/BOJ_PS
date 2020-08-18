// Problem No.: 13701
// Solver:      Jinmin Goh
// Date:        20200818
// URL: https://www.acmicpc.net/problem/13701

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

vector<bool> nums(33554440);

int main() {
    int n = 0, temp;
    while(scanf("%d", &temp) == 1) {
        if(nums[temp]) {
            continue;
        }
        nums[temp] = true;
        printf("%d ", temp);
    }

    return 0;
}