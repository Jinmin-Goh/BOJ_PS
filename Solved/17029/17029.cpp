// Problem No.: 17029
// Solver:      Jinmin Goh
// Date:        20200729
// URL: https://www.acmicpc.net/problem/17029

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

int main() {
    vector<string> character[110] = {};
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        char temp[30];
        int k;
        scanf("%s %d", temp, &k);
        for(int j = 0; j < k; j++) {
            char temp[30];
            scanf("%s", temp);
            string ch = temp;
            character[i].push_back(ch);
        }
    }
    int ans = 0;
    for(int i = 0; i < n - 1; i++) {
        for(int j = i + 1; j < n; j++) {
            int cnt = 0;
            for(int p = 0; p < character[i].size(); p++) {
                for(int q = 0; q < character[j].size(); q++) {
                    if(character[i].at(p) == character[j].at(q)) {
                        cnt++;
                    }
                }
            }
            ans = max(ans, cnt);
        }
    }
    printf("%d", ans + 1);
    return 0;
}