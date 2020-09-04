// Problem No.: 14938
// Solver:      Jinmin Goh
// Date:        20200903
// URL: https://www.acmicpc.net/problem/14938

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

int items[110], graph[110][110];

int main() {
    int n, m, r;
    scanf("%d %d %d", &n, &m, &r);
    for(int i = 1; i <= n; i++) {
        scanf("%d", &items[i]);
    }
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            if(i == j) continue;
            graph[i][j] = 1e9;
        }
    }
    for(int i = 1; i <= r; i++) {
        int a, b, w;
        scanf("%d %d %d", &a, &b, &w);
        graph[a][b] = w;
        graph[b][a] = w;
    }

    // for(int i = 1; i <= n; i++) {
    //     for(int j = 1; j <= n; j++) {
    //         printf("%d ", graph[i][j]);
    //     }
    //     printf("\n");
    // }

    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            for(int k = 1; k <= n; k++) {
                if(graph[j][k] > graph[j][i] + graph[i][k]) {
                    graph[j][k] = graph[j][i] + graph[i][k];
                }
            }
        }
    }

    // for(int i = 1; i <= n; i++) {
    //     for(int j = 1; j <= n; j++) {
    //         printf("%d ", graph[i][j]);
    //     }
    //     printf("\n");
    // }

    int ans = 0;
    for(int i = 1; i <= n; i++) {
        int tempAns = 0; 
        for(int j = 1; j <= n; j++) {
            if(graph[i][j] <= m) {
                tempAns += items[j];
            }
        }
        ans = max(ans, tempAns);
    }
    printf("%d", ans);
    
    return 0;
}