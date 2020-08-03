// Problem No.: 17197
// Solver:      Jinmin Goh
// Date:        20200803
// URL: https://www.acmicpc.net/problem/17197

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

int coordinates[100010][2], visited[100010];
vector<vector<int>> graph(100010);

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    for(int i = 1; i <= n; i++) {
        scanf("%d %d", &coordinates[i][0], &coordinates[i][1]);
    }
    for(int i = 0; i < m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    int ans = 1e9;

    // graph traversal
    for(int i = 1; i <= n; i++) {
        if(visited[i]) {
            continue;
        }
        int minX = coordinates[i][0], maxX = coordinates[i][0], minY = coordinates[i][1], maxY = coordinates[i][1];
        vector<int> stackList;
        stackList.push_back(i);
        while(stackList.size()) {
            int temp = stackList.back();
            stackList.pop_back();
            if(visited[temp]) {
                continue;
            }
            visited[temp] = true;
            minX = min(minX, coordinates[temp][0]);
            maxX = max(maxX, coordinates[temp][0]);
            minY = min(minY, coordinates[temp][1]);
            maxY = max(maxY, coordinates[temp][1]);
            stackList.insert(stackList.end(), graph[temp].begin(), graph[temp].end());
        }
        ans = min(ans, 2 * (maxX - minX + maxY - minY));
    }
    printf("%d", ans);
    return 0;
}