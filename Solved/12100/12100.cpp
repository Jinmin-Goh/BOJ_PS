// Problem No.: 12100
// Solver:      Jinmin Goh
// Date:        20200819
// URL: https://www.acmicpc.net/problem/12100

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

int table[20][20], ans, n;
queue<int> nums;

void get(int i, int j) {
    if (table[i][j]) {
        nums.push(table[i][j]);
        table[i][j] = 0;
    }
}

void merge(int i, int j, int di, int dj) {
    while (!nums.empty()) {
        int x = nums.front(); nums.pop();
        if (!table[i][j]) table[i][j] = x;
        else if (table[i][j] == x) {
            table[i][j] = x*2;
            i += di, j += dj;
        }
        else {
            i += di, j += dj;
            table[i][j] = x;
        }
    }   
}

void findFunc(int depth) {
    // move ended
    if(depth == 5) {
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                ans = max(ans, table[i][j]);
            }
        }
        return;
    }
    
    int tempTable[20][20];

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            tempTable[i][j] = table[i][j];
        }
    }

    for(int i = 0; i < 4; i++) {
        if(i == 0) {        // up
            for (int j = 0; j < n; j++) {
                for (int i = 0; i < n; i++) {
                    get(i, j);
                }
                merge(0, j, 1, 0);
            }
        }
        else if(i == 1) {   // down
            for (int j=0; j<n; j++) {
                for (int i=n-1; i>=0; i--) {
                    get(i, j);
                }
                merge(n-1, j, -1, 0);
            }
        }
        else if(i == 2) {   // left
            for (int i=0; i<n; i++) {
                for (int j=0; j<n; j++) {
                    get(i, j);
                }
                merge(i, 0, 0, 1);
            }
        }
        else {              // right
            for (int i=0; i<n; i++) {
                for (int j=n-1; j>=0; j--) {
                    get(i, j);
                }
                merge(i, n-1, 0, -1);
            }
        }

        findFunc(depth + 1);
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                table[i][j] = tempTable[i][j];
            }
        }
    }
    

}

int main() {
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            scanf("%d", &table[i][j]);
        }
    }

    findFunc(0);

    printf("%d", ans);
    return 0;
}