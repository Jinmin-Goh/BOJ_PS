// Problem No.: 18785
// Solver:      Jinmin Goh
// Date:        20200908
// URL: https://www.acmicpc.net/problem/18785

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

int clockList[2510], sumVal, visited[2510];
vector<vector<int>> graph(2510);

int main() {
    int n;
    scanf("%d", &n);
    for(int i = 1; i <= n; i++) {
        scanf("%d", &clockList[i]);
    }
    for(int i = 0; i < n - 1; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    int ans = 0;
    for(int i = 1; i <= n; i++) {
        sumVal = 0;
        queue<int> tempList;
        tempList.push(i);
        for(int i = 1; i <= n; i++) {
            visited[i] = 0;
        }
        int dist = 0;
        while(tempList.size()) {
            tempList.push(-1);
            while(true) {
                int temp = tempList.front();
                tempList.pop();

                if(temp == -1) break;
                if(visited[temp]) continue;
                visited[temp] = 1;
                if(dist % 2) {
                    sumVal -= clockList[temp];
                }
                else {
                    sumVal += clockList[temp];
                }
                sumVal %= 12;
                for(int j = 0; j < graph[temp].size(); j++) {
                    tempList.push(graph[temp][j]);
                }
            }
            dist++;
        }
        sumVal = (sumVal + 12) % 12;
        //printf("%d\n",sumVal); 
        if(sumVal == 0 || sumVal == 1) {
            ans++;
        }
    }
    printf("%d", ans);
    return 0;
}