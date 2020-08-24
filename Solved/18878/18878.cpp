// Problem No.: 18878
// Solver:      Jinmin Goh
// Date:        20200820
// URL: https://www.acmicpc.net/problem/18878

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

vector<pair<int, int>> favorite;
int owner[100010];
int ans[100010];
// map<int, int> firstList, secondList;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        favorite.push_back(make_pair(a, b));
    }
    

    int cnt = 0;
    for(int i = n - 1; i >= 0; i--) {
        int stealer = i, cereal = favorite[i].first;
        while(true) {
            if(!owner[cereal]) {
                owner[cereal] = stealer;
                cnt++;
                break;
            }
            else if(owner[cereal] < stealer) {
                break;
            }
            else {
                int p = owner[cereal];
                owner[cereal] = stealer;
                if(cereal == favorite[p].second) {
                    break;
                }
                stealer = p;
                cereal = favorite[p].second;
            }
        }
        ans[i] = cnt;
    }
    for(int i = 0; i < n; i++) {
        printf("%d\n", ans[i]);
    }
    return 0;
}