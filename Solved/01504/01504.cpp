// Problem No.: 1504
// Solver:      Jinmin Goh
// Date:        20200901
// URL: https://www.acmicpc.net/problem/1504

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

int cost[810], graph[810][810];
set<int> visited;
int n, e;

int dijkstra(int start, int end) {
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	pq.push(make_pair(0, start));
	for(int i = 1; i <= n; i++) {
		cost[i] = 1e9;
	}
	while(pq.size()) {
		int currNode = pq.top().second, currCost = pq.top().first;
		pq.pop();
		if(cost[currNode] < currCost) {
			continue;
		}
		cost[currNode] = currCost;
		for(int i = 1; i <= n; i++) {
			if(cost[i] > cost[currNode] + graph[currNode][i]) {
				cost[i] = cost[currNode] + graph[currNode][i];
				pq.push(make_pair(cost[i], i));
			}
		}
	}
	return cost[end];
}

int main() {
    scanf("%d %d", &n, &e);
	for(int i = 1; i <= n; i++) {
		for(int j = 1; j <= n; j++) {
			graph[i][j] = 1e8;
		}
	}
    for(int i = 0; i < e; i++) {
        int a, b, w;
        scanf("%d %d %d", &a, &b, &w);
		graph[a][b] = min(graph[a][b], w);
        graph[b][a] = min(graph[b][a], w);
    }
    int node1, node2;
    scanf("%d %d", &node1, &node2);

	int ans1 = dijkstra(1, node1) + dijkstra(node1, node2) + dijkstra(node2, n);
	int ans2 = dijkstra(1, node2) + dijkstra(node2, node1) + dijkstra(node1, n);
    // check start-node1-node2-end or start-node2-node1-end
	// from start
	if(min(ans1, ans2) >= 1e8) {
		printf("-1");
	}
	else {
		printf("%d", min(ans1, ans2));
	}

    return 0;
}