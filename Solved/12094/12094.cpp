// Problem No.: 12094
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

int n, ans;
int table[20][20];
int maxPerDepth[11];

void action(int actionVal) {
    queue<int> q;
    if(actionVal == 0){ // left
        for (int y = 0; y < n; ++y) {
            for (int x = 0; x < n; ++x) {
                if (table[y][x]) q.push(table[y][x]);
                table[y][x] = 0;
            }
            int curRowIdx = 0;
            while (!q.empty()) {
                int tempVar = q.front(); 
                q.pop();
                if (table[y][curRowIdx] == 0) {
                    table[y][curRowIdx] = tempVar;
                }
                else if (table[y][curRowIdx] == tempVar) {
                    table[y][curRowIdx++] += tempVar;
                }
                else {
                    table[y][++curRowIdx] = tempVar;
                }
            }
        }
    }
    
    else if(actionVal == 1) { // right
        for (int y = 0; y < n; ++y) {
            for (int x = n - 1; x >= 0; --x) {
                if (table[y][x]) q.push(table[y][x]);
                table[y][x] = 0;
            }
            int curRowIdx = n - 1;
            while (!q.empty()) {
                int tempVar = q.front(); 
                q.pop();
                if (table[y][curRowIdx] == 0) {
                    table[y][curRowIdx] = tempVar;
                }
                else if (table[y][curRowIdx] == tempVar) {
                    table[y][curRowIdx--] += tempVar;
                }
                else {
                    table[y][--curRowIdx] = tempVar;
                }
            }
        }
    }
    else if(actionVal == 2) {  // up
        for (int x = 0; x < n; ++x) {
            for (int y = 0; y < n; ++y) {
                if (table[y][x]) q.push(table[y][x]);
                table[y][x] = 0;
            }
            int curColIdx = 0;
            while (!q.empty()) {
                int tempVar = q.front(); 
                q.pop();
                if (table[curColIdx][x] == 0) {
                    table[curColIdx][x] = tempVar;
                }
                else if (table[curColIdx][x] == tempVar) {
                    table[curColIdx++][x] += tempVar;
                }
                else {
                    table[++curColIdx][x] = tempVar;
                }
            }
        }
    }
    else { // down
        for (int x = 0; x < n; ++x) {
            for (int y = n - 1; y >= 0; --y) {
                if (table[y][x]) q.push(table[y][x]);
                table[y][x] = 0;
            }
            int curColIdx = n - 1;
            while (!q.empty()) {
                int tempVar = q.front(); q.pop();
                if (table[curColIdx][x] == 0) {
                    table[curColIdx][x] = tempVar;
                }
                else if (table[curColIdx][x] == tempVar) {
                    table[curColIdx--][x] += tempVar;
                }
                else {
                    table[--curColIdx][x] = tempVar;
                }
            }
        }
    }
}
bool isSame(int tmp[20][20]) {
	for (int y = 0; y < n; ++y) 
        for (int x = 0; x < n; ++x)
			if (tmp[y][x] != table[y][x]) return false;
	return true;
}
int findMaxElement() {
    int var = 0;
    for (int y = 0; y < n; ++y) 
        for (int x = 0; x < n; ++x)
            var = max(var, table[y][x]);
    return var;
}
void copyArray(int a[20][20], int b[20][20]) {
    for (int y = 0; y < n; ++y)
        for (int x = 0; x < n; ++x)
            a[y][x] = b[y][x];
}
void solve(int depth) {
    int checkCurrMaxValue = findMaxElement();   
    if (checkCurrMaxValue <= maxPerDepth[depth]) return; 
    if (depth == 10) {
        ans = max(ans, checkCurrMaxValue);
        int expectMaxPerDepth = ans;
        while (depth > 0) {
            maxPerDepth[depth--] = expectMaxPerDepth;
            expectMaxPerDepth /= 2;
        }
        return;
    }   
    int tempTable[20][20];
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            tempTable[i][j] = table[i][j];
            
        }
    }

    for (int i = 0; i < 4; ++i) {   
        action(i);                  
        if (isSame(tempTable)) continue;
        solve(depth + 1);           
        copyArray(table, tempTable);
    }
}
int main() {
    scanf("%d", &n);
    for (int y = 0; y < n; ++y)
        for (int x = 0; x < n; ++x) 
            cin >> table[y][x];
    ans = findMaxElement();  
    solve(0);
    printf("%d", ans);
}