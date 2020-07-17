// Problem No.: 18265
// Solver:      Jinmin Goh
// Date:        20200718
// URL: https://www.acmicpc.net/problem/18265

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

int main(){
    int ans, n, division, remainder, nums[8] = {1, 2, 4, 7, 8, 11, 13, 14};
    scanf("%d", &n);
    division = (n - 1) / 8;
    remainder = (n - 1) % 8;
    ans = 15 * division + nums[remainder];
    printf("%d", ans);

    return 0;
}