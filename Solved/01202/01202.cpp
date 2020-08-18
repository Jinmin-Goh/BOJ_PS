// Problem No.: 1202
// Solver:      Jinmin Goh
// Date:        20200818
// URL: https://www.acmicpc.net/problem/1202

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

long long int bags[300010];
pair<int, int> jewel[300010];

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    for(int i = 0; i < n; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        jewel[i] = make_pair(a, b);
    }

    for(int i = 0; i < k; i++) {
        scanf("%lld", &bags[i]);
    }

    sort(jewel, jewel + n);
    sort(bags, bags + k);

    priority_queue<int> maxJewelValue;
    int pointer = 0;
    long long int ans = 0;
    for(int i = 0; i < k; i++) {
        while(pointer < n && jewel[pointer].first <= bags[i]) {
            maxJewelValue.push(jewel[pointer].second);
            pointer++;
        }
        if(maxJewelValue.size() == 0) {
            continue;
        }
        int temp = maxJewelValue.top();
        maxJewelValue.pop();
        ans += temp;
    }
    printf("%lld", ans);
    
    return 0;
}