// Problem No.: 14698
// Solver:      Jinmin Goh
// Date:        20200907
// URL: https://www.acmicpc.net/problem/14698

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
    long long t;
    long long modVal = 1e9 + 7;
    scanf("%lld", &t);
    for(long long _ = 0; _ < t; _++) {
        priority_queue<long long, vector<long long>, greater<long long>> pq;
        long long n;
        scanf("%lld", &n);
        for(long long i = 0; i < n; i++) {
            long long temp;
            scanf("%lld", &temp);
            pq.push(temp);
        }
        vector<long long> ans;
        while(pq.size() > 1) {
            long long temp1, temp2, temp = 1;
            temp1 = pq.top();
            pq.pop();
            temp2 = pq.top();
            pq.pop();
            temp = (temp1) * (temp2);
            pq.push(temp);
            ans.push_back(temp);
        }
        long long ansVal = 1;
        for(int i = 0; i < ans.size(); i++) {
            ansVal *= (ans[i] % modVal);
            ansVal %= modVal;
        }
        printf("%lld\n", ansVal % modVal);
    }
    return 0;
}