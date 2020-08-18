// Problem No.: 1939
// Solver:      Jinmin Goh
// Date:        20200818
// URL: https://www.acmicpc.net/problem/1939

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

int parent[10010];

int findParent(int node) {
    if(parent[node] == node) {
        return node;
    }
    parent[node] = findParent(parent[node]);
    return parent[node];
}

void unionFunc(int node1, int node2) {
    int p1 = findParent(node1), p2 = findParent(node2);

    parent[p2] = p1;
    return;
}

vector<vector<int>> graph(10010);
priority_queue<vector<int>> edgeWeight;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    

    for(int i = 0; i < m; i++) {
        int a, b, w;
        scanf("%d %d %d", &a, &b, &w);
        graph[a].push_back(b);
        graph[b].push_back(a);
        edgeWeight.push(vector<int> {w, a, b});
    }
    
    int startPoint, endPoint;
    scanf("%d %d", &startPoint, &endPoint);

    // find maximum spanning tree with union-find
    for(int i = 0; i < n; i++) {
        parent[i] = i;
    }
    vector<int> temp;
    while(findParent(startPoint) != findParent(endPoint)) {
        temp = edgeWeight.top();
        edgeWeight.pop();
        if(findParent(temp[1]) == findParent(temp[2])) {
            continue;
        }
        unionFunc(temp[1], temp[2]);
        
    }
    printf("%d", temp[0]);

    return 0;
}