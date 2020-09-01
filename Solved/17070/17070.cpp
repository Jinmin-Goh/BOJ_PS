// Problem No.: 17070
// Solver:      Jinmin Goh
// Date:        20200831
// URL: https://www.acmicpc.net/problem/17070

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

int table[16][16], dpTable[16][16][3], ans, moveRow[3] = {0, 1, 1}, moveCol[3] = {1, 0, 1};
int n;

void solve(int row, int col, int status) {
    if(row == n - 1 && col == n - 1) {
        ans++;
        return;
    }

    // horizontal, vertical, diagonal
    for(int i = 0; i < 3; i++) {
        if((i == 0 && status == 1) || (i == 1 && status == 0)) {
            continue;
        }
        if(row + moveRow[i] >= n || col + moveCol[i] >= n || table[row + moveRow[i]][col + moveCol[i]] == 1) {
            continue;
        }
        if(i == 2 && (table[row][col + 1] == 1 || table[row + 1][col] == 1)) {
            continue;
        }

        solve(row + moveRow[i], col + moveCol[i], i);
    }

}



int main() {
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            scanf("%d", &table[i][j]);
        }
    }
    
    solve(0, 1, 0);

    printf("%d", ans);
    
    return 0;
}