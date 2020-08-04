// Problem No.: 17026
// Solver:      Jinmin Goh
// Date:        20200804
// URL: https://www.acmicpc.net/problem/17026

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

int main() {
    int n, ans = 0;
    vector<pair<int, int>> coordinates;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        coordinates.push_back(pair<int, int> (a - b, a + b));
    }
    sort(coordinates.begin(), coordinates.end());
    
    vector<pair<int, int>>::iterator iter = coordinates.begin();
    int currMax = -1e9 - 1;
    while(iter != coordinates.end()) {
        int tempVal = iter->first;
        bool foundFlag = false;
        while(iter != coordinates.end() && iter->first == tempVal) {
            if(currMax < iter->second && !foundFlag) {
                ans++;
                foundFlag = true;
                currMax = iter->second;
            }
            currMax = max(currMax, iter->second);
            iter++;
        }
    }
    printf("%d", ans);
    return 0;
}