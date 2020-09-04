// Problem No.: 1238
// Solver:      Jinmin Goh
// Date:        20200903
// URL: https://www.acmicpc.net/problem/1238

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

vector<vector<pair<int, int>>> fgraph(1010), bgraph(1010);

int fdist[1010], bdist[1010];

int main() {
    int n, m, x;
    scanf("%d %d %d", &n, &m, &x);
    for(int i = 0; i < m; i++) {
        int a, b, w;
        scanf("%d %d %d", &a, &b, &w);
        fgraph[a].push_back(make_pair(b, w));
        bgraph[b].push_back(make_pair(a, w));
    }

    for(int i = 1; i <= n; i++) {
        if(i == x) {
            continue;
        }
        fdist[i] = 1e9;
        bdist[i] = 1e9;
    }

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> fpq, bpq;
    fpq.push(make_pair(0, x));
    while(fpq.size()) {
        int currNode = fpq.top().second, currCost = fpq.top().first;
        fpq.pop();
        if(currCost > fdist[currNode]) {
            continue;
        }
        fdist[currNode] = currCost;
        for(int i = 0; i < fgraph[currNode].size(); i++) {
            int tempNode = fgraph[currNode][i].first, tempCost = fgraph[currNode][i].second;
            if(fdist[tempNode] > fdist[currNode] + tempCost) {
                fdist[tempNode] = fdist[currNode] + tempCost;
                fpq.push(make_pair(fdist[tempNode], tempNode));
            }
        }
    }

    bpq.push(make_pair(0, x));
    while(bpq.size()) {
        int currNode = bpq.top().second, currCost = bpq.top().first;
        bpq.pop();
        if(currCost > bdist[currNode]) {
            continue;
        }
        bdist[currNode] = currCost;
        for(int i = 0; i < bgraph[currNode].size(); i++) {
            int tempNode = bgraph[currNode][i].first, tempCost = bgraph[currNode][i].second;
            if(bdist[tempNode] > bdist[currNode] + tempCost) {
                bdist[tempNode] = bdist[currNode] + tempCost;
                bpq.push(make_pair(bdist[tempNode], tempNode));
            }
        }
    }
    int ans = 0;
    for(int i = 1; i <= n; i++) {
        ans = max(ans, fdist[i] + bdist[i]);
    }
    printf("%d", ans);

    return 0;
}