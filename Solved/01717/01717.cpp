// Problem No.: 1717
// Solver:      Jinmin Goh
// Date:        20200728
// URL: https://www.acmicpc.net/problem/1717

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

int parent[1000010];
int rankList[1000010];

void unionFunc(int node1, int node2);
int findParent(int node);

// set union; rank optimization
void unionFunc(int node1, int node2) {
    int root1 = findParent(node1), root2 = findParent(node2);
    if(rankList[root2] > rankList[root1]) {
        swap(root1, root2);
    }
    parent[root2] = root1;
    if(rankList[root2] == rankList[root1]) {
        rankList[root1]++;
    }
    return;
}

// finding parent; path compression
int findParent(int node) {
    // found root
    if(parent[node] == node) {
        return node;
    }
    // search for parent & path compression
    parent[node] = findParent(parent[node]);
    return parent[node];
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    // initialization
    for(int i = 0; i <= n; i++) {
        parent[i] = i;
        rankList[i] = 1;
    }
    // query
    for(int i = 0; i < m; i++) {
        int q, a, b;
        scanf("%d %d %d", &q, &a, &b);
        if(q == 0) {
            if(a != b) {
                unionFunc(a, b);
            }
        }
        else if(q == 1) {
            if(a != b){
                int aRoot = findParent(a), bRoot = findParent(b);
                if(aRoot == bRoot) {
                    printf("YES\n");
                }
                else {
                    printf("NO\n");
                }
            }
            else {
                printf("YES\n");
            }
        }
    }
    return 0;
}