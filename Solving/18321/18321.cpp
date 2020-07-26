// Problem No.: 
// Solver:      Jinmin Goh
// Date:        20200726
// URL: https://www.acmicpc.net/problem/

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
    int n, m, cows[100010], a[100010], b[100010], w[100010];
    bool flag = true;
    // parsing
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++) {
        int temp;
        scanf("%d", &temp);
        if(cows[i] != temp) {
            if(cows[i] != i + 1) {
                flag = false
            }
        }
    }
    for(int i = 0; i < m; i++) {
        scanf("%d %d %d", &a[i], &b[i], &w[i]);
    }
    
    // no need to change
    if(flag) {
        printf("%d", -1);
        return
    }
    
    return 0;
}