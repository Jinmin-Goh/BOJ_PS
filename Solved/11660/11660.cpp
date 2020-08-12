// Problem No.: 11660
// Solver:      Jinmin Goh
// Date:        20200812
// URL: https://www.acmicpc.net/problem/11660

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

int nums[1025][1025], dpTable[1025][1025];

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            scanf("%d", &nums[i][j]);
        }
    }

    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            if(j == 1) {
                dpTable[i][j] = nums[i][j];
            }
            else {
                dpTable[i][j] = nums[i][j] + dpTable[i][j - 1];
            }
        }
    }
    for(int i = 1; i <= n; i++) {
        for(int j = 2; j <= n; j++) {
            dpTable[j][i] += dpTable[j - 1][i];
        }
    }

    for(int i = 0; i < m; i++) {
        int x1, y1, x2, y2;
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);

        printf("%d\n", dpTable[x2][y2] - dpTable[x2][y1 - 1] - dpTable[x1 - 1][y2] + dpTable[x1 - 1][y1 - 1]);
    }

    return 0;
}