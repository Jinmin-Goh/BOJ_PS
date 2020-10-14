// Problem No.: 15995
// Solver:      Jinmin Goh
// Date:        20201014
// URL: https://www.acmicpc.net/problem/15995

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

pair<int, int> exgcd(int a, int b) {
    pair<int, int> temp;
    if(a == 1 && b == 0) {
        temp = make_pair(1, 0);
        return temp;
    }
    temp = exgcd(b, a % b);
    pair<int, int> returnVal;
    returnVal.first = temp.second;
    returnVal.second = temp.first - temp.second * (a / b);
    return returnVal;
}

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    pair<int, int> ans = exgcd(a, b);
    ans.first %= b;
    if(ans.first < 0) {
        ans.first += b;
    }
    printf("%d", ans.first);
    return 0;
}