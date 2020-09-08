// Problem No.: 14167
// Solver:      Jinmin Goh
// Date:        20200904
// URL: https://www.acmicpc.net/problem/14167

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

vector<pair<long long, long long>> coord;
vector<vector<long long>> costList;

int parent[1010];

int findFunc(int node) {
    if(node == parent[node]) {
        return node;
    }
    parent[node] = findFunc(parent[node]);
    return parent[node];
}

void mergeFunc(int node1, int node2) {
    int p1 = findFunc(node1), p2 = findFunc(node2);

    parent[p2] = p1;
}


int main() {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        long long a, b;
        scanf("%lld %lld", &a, &b);
        coord.push_back(make_pair(a, b));
    }

    for(int i = 0; i < n - 1; i++) {
        for(int j = i + 1; j < n; j++) {
            long long temp = pow(coord[i].first - coord[j].first, 2) + pow(coord[i].second - coord[j].second, 2);
            long long cost = temp;
            vector<long long> tempV = {cost, i, j};
            costList.push_back(tempV);
        }
    }

    sort(costList.begin(), costList.end());

    int cnt = 1;
    for(int i = 1; i <= n; i++) {
        parent[i] = i;
    }

    vector<vector<long long>>::iterator iter;
    long long ans = 0;
    for(iter = costList.begin(); iter != costList.end(); iter++) {
        if(cnt >= n) break;

        vector<long long> tempV = *iter;
        if(findFunc(tempV[1]) == findFunc(tempV[2])) continue;
        mergeFunc(tempV[1], tempV[2]);
        ans = tempV[0];
        cnt++;
    }

    printf("%lld", ans);

    return 0;
}