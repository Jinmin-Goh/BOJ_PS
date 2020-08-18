// Problem No.: 1946
// Solver:      Jinmin Goh
// Date:        20200818
// URL: https://www.acmicpc.net/problem/1946

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

pair<int, int> grade[100010];

int main() {
    int t;
    scanf("%d", &t);
    for(int _ = 0; _ < t; _++) {
        int n;
        scanf("%d", &n);
        for(int i = 0; i < n; i++) {
            int a, b;
            scanf("%d %d", &a, &b);
            grade[i] = make_pair(a, b);
        }
        sort(grade, grade + n);

        int currMax = grade[0].second, ans = 1;
        for(int i = 1; i < n; i++) {
            if(currMax > grade[i].second) {
                ans++;
                currMax = grade[i].second;
            }
        }
        printf("%d\n", ans);
    }
    return 0;
}