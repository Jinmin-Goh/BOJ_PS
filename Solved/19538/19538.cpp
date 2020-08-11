// Problem No.: 19538
// Solver:      Jinmin Goh
// Date:        20200807
// URL: https://www.acmicpc.net/problem/19538

#include <cassert>
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

int beliving[200010], visited[200010];
vector<vector<int>> graph(200010);

int main() {
    int n, m;
    scanf("%d", &n);
    for(int i = 1; i <= n; i++) {
        while(true){
			int a;
			cin >> a;
			if (!a) break;
			graph[i].push_back(a);
		}
    }
    for(int i = 0; i <= n; i++) {
        beliving[i] = -1;
    }
    scanf("%d", &m);
    queue<pair<int, int>> stackList;
    for(int i = 0; i < m; i++) {
        int temp;
        scanf("%d", &temp);
        stackList.push(make_pair(temp, 0));
        beliving[temp] = 0;
    }
    
    while (!stackList.empty()) {
		int node = stackList.front().first, timeVal = stackList.front().second;
        stackList.pop();
		for (auto temp : graph[node]) {
			if (beliving[temp] == -1) {
				int cnt = 0;
				for (auto temp2 : graph[temp]) {
					if ((beliving[temp2] != -1) && (beliving[temp2] <= timeVal)) {
						cnt += 1;
					}
				}
				int sizeVal = graph[temp].size();
				if (cnt >= (sizeVal + 1) / 2) {
					beliving[temp] = timeVal + 1;
					stackList.push(make_pair(temp, timeVal + 1));
				}
			}
		}
	}
    

    //assert(n > 100000);
    for(int i = 1; i <= n; i++) {
        printf("%d ", beliving[i]);
    }

    return 0;
}