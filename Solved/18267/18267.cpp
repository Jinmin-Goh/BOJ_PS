// Problem No.: 18267
// Solver:      Jinmin Goh
// Date:        20200720
// URL: https://www.acmicpc.net/problem/18267

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


int main(){
    int n, m;
    scanf("%d %d", &n, &m);
    // graph parsing
    vector<int> graph[100010];
    char nodeType[100010], ans[100010];
    int nodeGroup[100010] = {};
    scanf("%s", nodeType + 1);
    for (int i = 1; i < n; i++){
        int u, v;
        scanf("%d %d", &u, &v);
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    // separate group with breed by dfs
    int cnt(1);
    for(int i = 1; i <= n; i++){
        // visited node
        if(nodeGroup[i] != 0){
            continue;
        }
        bool typeH = false;
        if(nodeType[i] == 'H'){
            typeH = true;
        }
        vector<int> stackList;    // stack for dfs
        stackList.push_back(i);

        // if breeder is H
        if(typeH){
            while(stackList.size() > 0){
                int temp = stackList.back();
                stackList.pop_back();
                // if current node's breeder is not H or already visited; pass
                if(nodeType[temp] != 'H' || nodeGroup[temp] != 0){
                    continue;
                }
                nodeGroup[temp] = cnt;
                vector< int >::iterator iter = graph[temp].begin();

                for(iter; iter != graph[temp].end(); iter++){
                    stackList.push_back(*iter);
                }

            }
        }
        // if breeder is G
        else{
            while(stackList.size() > 0){
                int temp = stackList.back();
                stackList.pop_back();
                // if current node's breeder is H or already visited; pass
                if(nodeType[temp] == 'H' || nodeGroup[temp] != 0){
                    continue;
                }
                nodeGroup[temp] = cnt;
                vector< int >::iterator iter = graph[temp].begin();

                for(iter; iter != graph[temp].end(); iter++){
                    stackList.push_back(*iter);
                }

            }
        }
        cnt++;
    }

    // query check
    for(int i = 0; i < m; i++){
        int a, b;
        char c;
        scanf("%d %d %c", &a, &b, &c);
        if(nodeType[a] == c || nodeType[b] == c || nodeGroup[a] != nodeGroup[b]){
            printf("1");
        }
        else{
            printf("0");
        }
    }

    return 0;
}