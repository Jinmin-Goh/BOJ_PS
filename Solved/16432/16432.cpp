// Problem No.: 16432
// Solver:      Jinmin Goh
// Date:        20200915
// URL: https://www.acmicpc.net/problem/16432

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

int table[1010][15], dpTable[1010][15], ans[1010];
int n;

bool solve(int curr, int prev) {
    if(curr == n - 1) {
        for(int i=1;i<10;i++){
            if(i == prev) continue;
            if(table[curr][i]){
                ans[curr] = i;
                return true;
            }
        }
    }
    for(int i=1;i<10;i++) {
        if(i == prev) continue;
        if(table[curr][i] && !dpTable[curr][i]) {
            dpTable[curr][i] = 1;
            ans[curr] = i;
            if(solve(curr + 1, i)) {
                return true;
            }
        }
    }

    return false;
}

int main() {
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        int temp;
        scanf("%d", &temp);
        for(int j = 0; j < temp; j++) {
            int a;
            scanf("%d", &a);
            table[i][a] = 1;
        }
    }
    if(solve(0, 0)) {
        for(int i = 0; i < n; i++) {
            printf("%d\n", ans[i]);
        }
    }
    else {
        printf("-1");
    }
    return 0;
}