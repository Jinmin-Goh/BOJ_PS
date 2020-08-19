// Problem No.: 1495
// Solver:      Jinmin Goh
// Date:        20200818
// URL: https://www.acmicpc.net/problem/1495

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

int dpTable[110][1010], deltaList[110];

int main() {
    int n, s, m;
    scanf("%d %d %d", &n, &s, &m);
    for(int i = 0; i < n; i++) {
        scanf("%d", &deltaList[i]);
    }
    dpTable[0][s] = 1;
    for(int i = 0; i < n; i++) {
        bool flag = false;
        for(int j = 0; j <= m; j++) {
            if(dpTable[i][j]) {
                if(j - deltaList[i] >= 0) {
                    flag = true;
                    dpTable[i + 1][j - deltaList[i]] = 1;
                }
                if(j + deltaList[i] <= m) {
                    flag = true;
                    dpTable[i + 1][j + deltaList[i]] = 1;
                }
            }
        }
        if(!flag) {
            printf("-1");
            return 0;
        }
    }
    for(int i = m; i >= 0; i--) {
        if(dpTable[n][i]) {
            printf("%d", i);
            return 0;
        }
    }

    return 0;
}