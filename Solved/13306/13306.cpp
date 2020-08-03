// Problem No.: 13306
// Solver:      Jinmin Goh
// Date:        20200803
// URL: https://www.acmicpc.net/problem/13306

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

int inputParent[200010], currParent[200010], query[400010][3];
string ans[200010];

int parentFind(int node) {
    if(currParent[node] == node) {
        return node;
    }

    currParent[node] = parentFind(currParent[node]);
    return currParent[node];
}

void unionFunc(int node1, int node2) {
    int par1 = parentFind(node1), par2 = parentFind(node2);
    if(par1 == par2) {
        return;
    }
    currParent[par2] = par1;
}

int main() {
    int n, q;
    scanf("%d %d", &n, &q);
    // parent parsing
    for(int i = 2; i <= n; i++) {
        scanf("%d", &inputParent[i]);
    }
    // query parsing
    for(int i = 0; i < n - 1 + q; i++) {
        scanf("%d", &query[i][0]);
        if(query[i][0] == 0) {
            scanf("%d", &query[i][1]);
        }
        else {
            scanf("%d %d", &query[i][1], &query[i][2]);
        }
    }
    // parent initialization
    for(int i = 1; i <= n; i++) {
        currParent[i] = i;
    }
    
    // reversed query process
    int ansPointer = 0;
    for(int i = n + q - 2; i >= 0; i--) {
        // union
        if(query[i][0] == 0) {
            unionFunc(parentFind(query[i][1]), inputParent[query[i][1]]);
        }
        // find
        else {
            if(parentFind(query[i][1]) == parentFind(query[i][2])) {
                ans[q - 1 - ansPointer] = "YES";
            }
            else {
                ans[q - 1 - ansPointer] = "NO";
            }
            ansPointer++;
        }
    }

    for(int i = 0; i < q; i++) {
        printf("%s\n", ans[i].c_str());
    }

    return 0;
}