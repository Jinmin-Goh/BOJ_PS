// Problem No.: 19535
// Solver:      Jinmin Goh
// Date:        20200807
// URL: https://www.acmicpc.net/problem/19535

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

int n;
vector<vector<int>> graph(300010);
vector<pair<int, int>> edges;

int main() {
    scanf("%d", &n);
    for(int i = 0; i < n - 1; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        edges.push_back(make_pair(a, b));
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    long long int dCnt = 0, gCnt = 0;
    for(int i = 0; i < n - 1; i++) {
        long long int a = edges[i].first, b = edges[i].second;
        dCnt += (graph[a].size() - 1) * (graph[b].size() - 1);
    }
    for(int i = 1; i <= n; i++) {
        if(graph[i].size() > 2) {
            long long int temp = graph[i].size();
            gCnt += temp * (temp - 1) * (temp - 2) / 6;
        }
    }

    if(dCnt > gCnt * 3) {
        printf("D");
    }
    else if(dCnt < gCnt * 3) {
        printf("G");
    }
    else {
        printf("DUDUDUNGA");
    }

    return 0;
}