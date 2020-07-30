// Problem No.: 
// Solver:      Jinmin Goh
// Date:        20200726
// URL: https://www.acmicpc.net/problem/

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

int findParent(int n, int* parents) {
    if(parents[n] == n) {
        return n;
    }
    parents[n] = findParent(parents[n], parents);
    return parents[n];
}

void unionFunc(int n1, int n2, int* parents) {
    int r1 = findParent(n1, parents), r2 = findParent(n2, parents);
    parents[r1] = r2;
    return;
}

int main() {
    int n, m, cows[100010], a[100010], b[100010], w[100010];
    vector<int> diffNode;
    vector<vector<int>> edge;
    bool flag = true;
    // parsing
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++) {
        scanf("%d", &cows[i]);
        if(cows[i] != i + 1) {
            flag = false;
            diffNode.push_back(i + 1);
        }
    }
    for(int i = 0; i < m; i++) {
        scanf("%d %d %d", &a[i], &b[i], &w[i]);
        edge.push_back(vector<int> {w[i], a[i], b[i]});
    }
    sort(edge.begin(), edge.end());

    // no need to change
    if(flag) {
        printf("%d", -1);
        return 0;
    }

    // do binary search for answer
    int left = 0, right = m - 1;
    while(left < right) {
        int mid = (left + right + 1) / 2;
        bool connectFlag = true;

        // do union(for connected components) - find(check whether all different components are connected)
        int parents[100010] = {}, visited[100010] = {};
        for(int i = 1; i <= n; i++) {
            parents[i] = i;
        }
        for(int i = mid; i < m; i++) {
            unionFunc(edge.at(i).at(1), edge.at(i).at(2), parents);
        }

        // check connectivity; finding process
        vector<int>::iterator iter;
        int tempParent = findParent(diffNode.front(), parents);
        for(iter = diffNode.begin(); iter != diffNode.end(); iter++) {
            if(findParent(*iter, parents) != tempParent) {
                connectFlag = false;
                break;
            }
        }

        if(connectFlag) {
            left = mid;
        }
        else {
            right = mid - 1;
        }
    }
    printf("%d", edge.at(left).at(0));
    
    return 0;
}