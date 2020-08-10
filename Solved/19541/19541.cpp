// Problem No.: 19541
// Solver:      Jinmin Goh
// Date:        20200810
// URL: https://www.acmicpc.net/problem/19541

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

int infected[100010], finalStatus[100010], checkStatus[100010], initStatus[100010], appear[100010];
vector<vector<int>> query;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    for(int i = 0; i < m; i++) {
        int a;
        scanf("%d", &a);
        vector<int> temp(a);
        for(int j = 0; j < a; j++) {
            scanf("%d", &temp[j]);
            appear[temp[j]] = 1;
        }
        query.push_back(temp);
    }
    for(int i = 1; i <= n; i++) {
        scanf("%d", &finalStatus[i]);
    }

    for(int i = 1; i <= n; i++) {
        infected[i] = finalStatus[i];
    }

    // reverse check & find initially not infected person
    for(int i = m - 1; i >= 0; i--) {
        bool notFlag = false;
        int sizeVal = query[i].size();
        for(int j = sizeVal - 1; j >= 0; j--) {
            if(infected[query[i][j]] == 0) {
                notFlag = true;
            }
        }
        if(notFlag) {
            for(int j = sizeVal - 1; j >= 0; j--) {
                infected[query[i][j]] = 0;
            }   
        }
    }

    // reverse infected to initial status
    for(int i = 1; i <= n; i++) {
        if(infected[i] == 1) {
            initStatus[i] = 1;
            checkStatus[i] = 1;
        }
    }

    // check query
    for(int i = 0; i < m; i++) {
        bool infectFlag = false;
        int sizeVal = query[i].size();
        for(int j = sizeVal - 1; j >= 0; j--) {
            if(checkStatus[query[i][j]] == 1) {
                infectFlag = true;
            }
        }
        if(infectFlag) {
            for(int j = sizeVal - 1; j >= 0; j--) {
                checkStatus[query[i][j]] = 1;
            }   
        }
    }

    // compare given final status and rebuilt final status
    for(int i = 1; i <= n; i++) {
        if(checkStatus[i] != finalStatus[i]) {
            if(!appear[i]) {
                continue;
            }
            else {
                printf("NO");
                return 0;
            }
        }
    }
    printf("YES\n");
    for(int i = 1; i <= n; i++) {
        printf("%d ", initStatus[i]);
    }

    return 0;
}