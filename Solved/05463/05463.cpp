// Problem No.: 5463
// Solver:      Jinmin Goh
// Date:        20200804
// URL: https://www.acmicpc.net/problem/5463

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

int n, m;
int table[51][51], raisins[51][51], dpTable[51][51][51][51] = {-1};    // x1,y1, x2, y2


int solve(int x1, int y1, int x2, int y2)
{
    if (dpTable[x1][y1][x2][y2] == -1)  // not computed
    {
        // single case; no cost
        if (x1 == x2 && y1 == y2) {
            dpTable[x1][y1][x2][y2] = 0;
        }
        // multiple case; costs
        else {
            int minVal = 100000000;
            // row
            for (int x = x1 + 1; x <= x2; x++)
            {
                int payment = solve(x1, y1, x - 1, y2) + solve(x, y1, x2, y2);
                minVal = min(minVal, payment);
            }
            //col
            for (int y = y1 + 1; y <= y2; y++)
            {
                int payment = solve(x1, y1, x2, y - 1) + solve(x1, y, x2, y2);
                minVal = min(minVal, payment);
            }
            // calculate raisins
            int base_raisins = raisins[x2][y2];
            if (x1 > 0)
                base_raisins -= raisins[x1 - 1][y2];
            if (y1 > 0)
                base_raisins -= raisins[x2][y1 - 1];
            if (x1 > 0 && y1 > 0)
                base_raisins += raisins[x1 - 1][y1 - 1];

            dpTable[x1][y1][x2][y2] = minVal + base_raisins;
        }
    }
    return dpTable[x1][y1][x2][y2];
}


int main() {
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            scanf("%d", &table[i][j]);
        }
    }
    
    for(int x1 = 0; x1 < 50; x1++) {
        for(int y1 = 0; y1 < 50; y1++) {
            for(int x2 = 0; x2 < 50; x2++) {
                for(int y2 = 0; y2 < 50; y2++) {
                    dpTable[x1][y1][x2][y2] = -1;
                }
            }
        }
    }

    raisins[0][0] = table[0][0];
    for(int i = 1; i < n; i++) {
        raisins[i][0] = table[i][0] + raisins[i - 1][0];
    }
    for(int i = 1; i < m; i++) {
        raisins[0][i] = table[0][i] + raisins[0][i - 1];
    }

    for(int i = 1; i < n; i++) {
        for(int j = 1; j < m; j++) {
            raisins[i][j] = table[i][j] + raisins[i - 1][j] + raisins[i][j - 1] - raisins[i - 1][j - 1];
        }
    }
    printf("%d", solve(0, 0, n - 1, m - 1));
    return 0;
}