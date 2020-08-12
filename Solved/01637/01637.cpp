// Problem No.: 1637
// Solver:      Jinmin Goh
// Date:        20200812
// URL: https://www.acmicpc.net/problem/1637

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

int n;
vector<vector<long long int>> dataList;

long long int cntFunc(long long int mid) {
    int cnt = 0;
    for(int i = 0; i < n; i++) {
        if(dataList[i][0] > mid) {
            continue;
        }
        
        cnt += (min(mid, dataList[i][1]) - dataList[i][0]) / dataList[i][2] + 1;
    }
    return cnt;
}

int main() {
    scanf("%d", &n);
    
    for(int i = 0; i < n; i++) {
        long long int a, b, c;
        scanf("%lld %lld %lld", &a, &c, &b);
        vector<long long int> temp = {a, c ,b};
        dataList.push_back(temp);
    }

    long long int lo = 0, hi = 2147483648;
    while(lo < hi) {
        
        long long int mid = (lo + hi) / 2, cnt = 0;
        cnt = cntFunc(mid);
        if(cnt % 2) {
            hi = mid;
        }
        else {
            lo = mid + 1;
        }
    }

    if(lo == 2147483648) {
        printf("NOTHING");
        return 0;
    }
    printf("%lld %lld", lo, cntFunc(lo) - cntFunc(lo - 1));

    

    return 0;
}