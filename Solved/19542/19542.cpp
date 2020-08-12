// Problem No.: 19542
// Solver:      Jinmin Goh
// Date:        20200810
// URL: https://www.acmicpc.net/problem/19542

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

vector<vector<int>> graph(100010);
int depth[100010];
int n, s, d, ans;

int depthDFS(int upNode, int currNode) {
    // leaf node
    if(graph[currNode].size() == 1 && currNode != s) {
        depth[currNode] = 0;
        return 1;
    }
    
    int depthVal = 0;
    for(int i = 0; i < graph[currNode].size(); i++) {
        if(graph[currNode][i] == upNode) {
            continue;
        }
        depthVal = max(depthVal, depthDFS(currNode, graph[currNode][i]));
    }
    depth[currNode] = depthVal;
    return depthVal + 1;
}

void cntDFS(int upNode, int currNode) {
    if(depth[currNode] < d) {
        return;
    }

    for(int i = 0; i < graph[currNode].size(); i++) {
        if(depth[graph[currNode][i]] >= d) {
            ans += 1;
        }
        if(graph[currNode][i] != upNode) {
            cntDFS(currNode, graph[currNode][i]);
        }
    }
    return;
}

int main() {
    scanf("%d %d %d", &n, &s, &d);
    for(int i = 0; i < n - 1; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    // do DFS once and record depth
    depthDFS(-1, s);
    cntDFS(-1, s);
    printf("%d", ans);
    return 0;
}