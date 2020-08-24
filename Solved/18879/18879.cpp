// Problem No.: 18879
// Solver:      Jinmin Goh
// Date:        20200820
// URL: https://www.acmicpc.net/problem/18879

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



int parent[100010], minVal[100010], maxVal[100010];
vector<pair<int, int>> spins;
map<pair<int, int>, int> indexMap;

bool sortFunc(const pair<int,int> &a, const pair<int,int> &b) { 
    return (a.second < b.second);
} 

int main() {
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        spins.push_back(make_pair(a, b));
        indexMap[make_pair(a, b)] = i;
    }
    sort(spins.begin(), spins.end());

    minVal[0] = spins[0].second;
    for(int i = 1; i < n; i++) {
        minVal[i] = min(minVal[i - 1], spins[i].second);
    }

    maxVal[n - 1] = spins[n - 1].second;
    for(int i = n - 2; i >= 0; i--) {
        maxVal[i] = max(maxVal[i + 1], spins[i].second);
    }
    int ans = 1;
    for(int i = 0; i < n - 1; i++) {
        if(minVal[i] > maxVal[i + 1]) {
            ans++;
        }
    }
    printf("%d", ans);
}




// int parent[100010];
// vector<pair<int, int>> spins;
// map<pair<int, int>, int> indexMap;


// int findParent(int node) {
//     if(parent[node] == node) {
//         return node;
//     }
//     parent[node] = findParent(parent[node]);
//     return parent[node];
// }

// void mergeParent(int node1, int node2) {
//     int p1 = findParent(node1), p2 = findParent(node2);
//     if(p1 == p2) return;
//     parent[p2] = p1;
//     return;
// }

// bool sortFunc(const pair<int,int> &a, const pair<int,int> &b) { 
//     return (a.second < b.second);
// } 

// int main() {
//     int n;
//     scanf("%d", &n);
//     for(int i = 0; i < n; i++) {
//         int a, b;
//         scanf("%d %d", &a, &b);
//         spins.push_back(make_pair(a, b));
//         indexMap[make_pair(a, b)] = i;
//     }
    
//     for(int i = 0; i < n; i++) {
//         parent[i] = i;
//     }

//     sort(spins.begin(), spins.end());

//     int maxVal = spins[n - 1].second, currParent = findParent(indexMap[spins[n - 1]]);
//     for(int i = n - 2; i >= 0; i--) {
//         if(spins[i].second > maxVal) {
//             currParent = findParent(indexMap[spins[i]]);
//             maxVal = spins[i].second;
//         }
//         else {
//             mergeParent(currParent, indexMap[spins[i]]);
//         }
//     }

//     sort(spins.begin(), spins.end(), sortFunc);

//     maxVal = spins[n - 1].first;
//     currParent = findParent(indexMap[spins[n - 1]]);

//     for(int i = n - 2; i >= 0; i--) {
//         if(spins[i].first > maxVal) {
//             currParent = findParent(indexMap[spins[i]]);
//             maxVal = spins[i].first;
//         }
//         else {
//             mergeParent(currParent, indexMap[spins[i]]);
//         }
//     }
//     set<int> ansSet;
//     for(int i = 0; i < n; i++) {
//         ansSet.insert(findParent(parent[i]));
//     }
//     printf("%ld", ansSet.size());

//     return 0;
// }