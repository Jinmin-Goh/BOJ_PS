// Problem No.: 14658
// Solver:      Jinmin Goh
// Date:        20201013
// URL: https://www.acmicpc.net/problem/14658

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

pair<int, int> coord[110];

int main() {
    int n, m, l, k;
    scanf("%d %d %d %d", &n, &m, &l, &k);
    for(int i = 0; i < k; i++) {
        scanf("%d %d", &coord[i].first, &coord[i].second);
    }

    int ans = 0;
    for(int i = 0; i < k; i++) {
        for(int j = 0; j < k; j++) {
            int cnt = 0;
            for(int p = 0; p < k; p++) {
                if (coord[i].first <= coord[p].first && coord[p].first <= coord[i].first + l && coord[j].second <= coord[p].second && coord[p].second <= coord[j].second + l) {
                    cnt++;
                }
            }
            ans = max(ans, cnt);
        }
    }
    printf("%d", k - ans);
    return 0;
}