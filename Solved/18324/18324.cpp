// Problem No.: 18324
// Solver:      Jinmin Goh
// Date:        20200720
// URL: https://www.acmicpc.net/problem/18324

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

int helper(int minSpeed, int dist) {
    int lDist = 0, rDist = 0, time = 0, currSpeed = 1;
    while(1) {
        lDist += currSpeed;
        time++;
        if(lDist + rDist >= dist) {
            return time;
        }
        if(currSpeed >= minSpeed) {
            rDist += currSpeed;
            time++;
            if(lDist + rDist >= dist) {
                return time;
            }    
        }
        currSpeed++;
    }
}

int main() {
    int n, k, val;
    scanf("%d %d", &k, &n);
    
    for(int i = 0; i < n; i++) {
        int minSpeed, ans;
        scanf("%d", &minSpeed);
        ans = helper(minSpeed, k);
        printf("%d\n", ans);
    }

    return 0;
}