// Problem No.: 1774
// Solver:      Jinmin Goh
// Date:        20201004
// URL: https://www.acmicpc.net/problem/1774

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

int n, m, v1, v2, par[1002], X[1002], Y[1002];


int findParent(int x){
    if(par[x] == x)return x;
    return par[x] = findParent(par[x]);
}

int mergeFunc(int x, int y){
    int px = findParent(x), py = findParent(y);
    if(px == py)return 0;
    par[px] = py;
    return 1;
}

int main(){
    double ans = 0;
    scanf("%d %d", &n, &m);
    for(int i = 1; i <= n; i++){
        scanf("%d %d", &X[i], &Y[i]);
        par[i] = i;
    }
    for(int i = 0; i < m; i++){
        scanf("%d %d", &v1, &v2);
        mergeFunc(v1, v2);
    }
    priority_queue<pair<double, pair<int, int>>> pq;
    for(int i = 1; i <= n; i++){
        for(int j = i + 1; j <= n; j++){
            double d = (long long) (X[i] - X[j]) * (X[i] - X[j]) + (long long) (Y[i] - Y[j]) * (Y[i] - Y[j]);
            pq.push(pair<double, pair<int, int>>(-d, pair<int, int>(i, j)));
        }
    }
    int cnt = m;
    while(!pq.empty() && cnt != n - 1) {
        pair<double, pair<int, int>> top = pq.top(); pq.pop();
        double tv = top.first;
        int tx = top.second.first, ty = top.second.second;
        if(mergeFunc(tx, ty))ans += sqrt(-tv), cnt++;
    }
    printf("%.2f", ans);
}