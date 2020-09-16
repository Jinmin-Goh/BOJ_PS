// Problem No.: 5546
// Solver:      Jinmin Goh
// Date:        20200915
// URL: https://www.acmicpc.net/problem/5546

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

int pasta[110], dpTable[110][5][5]; // dpTable[i][j][k]: i번째 날에 j파스타를 k일 연속 먹은 경우

int main() {
    int n, k, modVal = 10000;
    scanf("%d %d", &n, &k);
    for(int i = 0; i < k; i++) {
        int day, temp;
        scanf("%d %d", &day, &temp);
        pasta[day] = temp;
    }

    if(pasta[1]) {
        dpTable[1][pasta[1]][1] = 1;
    }
    else {
        dpTable[1][1][1] = 1;
        dpTable[1][2][1] = 1;
        dpTable[1][3][1] = 1;
    }

    for(int i = 2; i <= n; i++) {
        // pasta
        for(int j = 1; j <= 3; j++) {
            if(pasta[i] && pasta[i] != j) continue;
            // prev pasta
            for(int k = 1; k <= 3; k++) {
                if(j == k) {
                    dpTable[i][j][2] = dpTable[i - 1][k][1];
                    dpTable[i][j][2] %= modVal;
                }
                else {
                    dpTable[i][j][1] += dpTable[i - 1][k][1] + dpTable[i - 1][k][2];
                    dpTable[i][j][1] %= modVal;
                }
            }
        }
    }

    int ans = 0;
    for(int i = 1; i <= 3; i++) {
        ans += dpTable[n][i][1] + dpTable[n][i][2];
        ans %= modVal;
    }
    
    printf("%d", ans);
    return 0;
}