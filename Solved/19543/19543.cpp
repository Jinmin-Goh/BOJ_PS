// Problem No.: 19543
// Solver:      Jinmin Goh
// Date:        20200811
// URL: https://www.acmicpc.net/problem/19543

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

char bulidingList[200010];
vector<char> query;
map<char, string> mappingList;

int findFunc(int topVal, int lVal, int rVal) {
    for(int i = rVal; i >= lVal; i--) {
        if(mappingList[topVal][i] == 'U') {
            return i;
        }
    }
    return -1;
}

int main() {
    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);
    for(int i = 0; i < k; i++) {
        char temp[200010], AVal = 'A';
        scanf("%s", temp);
        mappingList[AVal + i] = string(temp);
    }
    scanf("%s", bulidingList);
    for(int i = 0; i < n; i++) {
        query.push_back(bulidingList[i]);
    }

    long long int ans = 0;
    int lVal = m - 1, rVal = m - 1;
    char topVal = query.back();
    query.pop_back();
    while(lVal > 0 && mappingList[topVal][lVal - 1] != 'U') {
        lVal--;
    }

    while(query.size() > 0) {
        ans += rVal - lVal + 1;
        topVal = query.back();
        query.pop_back();
        rVal = findFunc(topVal, lVal, rVal);
        if(rVal == -1) {
            break;
        }
        lVal = findFunc(topVal, 0, lVal - 1) + 1;
    }
    if(rVal != -1) {
        ans += rVal - lVal + 1;
    }
    printf("%lld", ans);
    

    return 0;
}