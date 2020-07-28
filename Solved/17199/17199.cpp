// Problem No.: 17199
// Solver:      Jinmin Goh
// Date:        20200727
// URL: https://www.acmicpc.net/problem/17199

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

int main() {
    int n;
    scanf("%d", &n);
    vector<vector<int>> graph(110);

    for(int i = 0; i < n - 1; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        graph.at(b).push_back(a);
    }
    for(int i = 1; i <= n; i++) {
        int visited[110] = {};
        vector<int> stackList;
        stackList.push_back(i);
        int checkCnt = 0;
        while(stackList.size() > 0) {
            int temp = stackList.back();
            stackList.pop_back();
            if(visited[temp]) {
                continue;
            }
            visited[temp] = 1;
            checkCnt++;
            stackList.insert(stackList.end(), graph.at(temp).begin(), graph.at(temp).end());
        }
        
        if(checkCnt == n) {
            printf("%d", i);
            return 0;
        }

    }
    printf("%d", -1);
    return 0;
}