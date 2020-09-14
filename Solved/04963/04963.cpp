// Problem No.: 4963
// Solver:      Jinmin Goh
// Date:        20200914
// URL: https://www.acmicpc.net/problem/4963

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

int table[55][55], dx[8] = {1, -1, 0, 0, 1, 1, -1, -1}, dy[8] = {0, 0, 1, -1, 1, -1, 1, -1};

int main() {
    
    int w, h;
    scanf("%d %d", &w, &h);
    while(w != 0 && h != 0) {
        for(int i = 0; i < h; i++) {
            for(int j = 0; j < w; j++) {
                scanf("%d", &table[i][j]);
            }
        }
        int ans = 0;
        for(int i = 0; i < h; i++) {
            for(int j = 0; j < w; j++) {
                if(table[i][j] == 1) {
                    ans++;
                    queue<pair<int, int> > tempList;
                    tempList.push(make_pair(i, j));
                    while(tempList.size()) {
                        pair<int, int> temp = tempList.front();
                        tempList.pop();
                        int x = temp.first, y = temp.second;
                        if(table[x][y] != 1) continue;
                        table[x][y] = 0;
                        for(int k = 0; k < 8; k++) {
                            if(x + dx[k] >= 0 && x + dx[k] < h && y + dy[k] >= 0 && y + dy[k] < w ) {
                                tempList.push(make_pair(x + dx[k], y + dy[k]));
                            }
                        }
                    }
                }
            }
        }
        printf("%d\n", ans);
        scanf("%d %d", &w, &h);
    }   
    return 0;
}