// Problem No.: 1708
// Solver:      Jinmin Goh
// Date:        20220711
// URL: https://www.acmicpc.net/problem/1708

#include <iostream>
#include <algorithm>
#include <iterator>
#include <stack>
#include <vector>
using namespace std;

typedef long long lli;

int ccw(pair< lli, lli > a, pair< lli, lli > b, pair< lli, lli > c) {
    lli val1 = a.first * b.second + b.first * c.second + c.first * a.second, val2 = b.first * a.second + c.first * b.second + a.first * c.second;
    if ((val1 - val2) > 0)
        return 1;
    else if ((val1 - val2) < 0) 
        return -1;
    else
        return 0;
}

int main() {
    int n;
    vector< pair< lli, lli > > dots;
    vector< lli > s;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        lli a, b;
        scanf("%lld %lld", &a, &b);
        dots.push_back(pair< lli, lli >(a, b));
    }
    sort(dots.begin(), dots.end());
    dots.erase(unique(dots.begin(), dots.end()), dots.end());
    sort(next(dots.begin()), dots.end(), [&](const pair< lli, lli > &left, const pair< lli, lli > &right) {
        if ((left.second - dots[0].second) * (right.first - dots[0].first) == (right.second - dots[0].second) * (left.first - dots[0].first))
            return (left.second - dots[0].second) * (left.second - dots[0].second) + (left.first - dots[0].first) * (left.first - dots[0].first) < (right.second - dots[0].second) * (right.second - dots[0].second) + (right.first - dots[0].first) * (right.first - dots[0].first);
        return (left.second - dots[0].second) * (right.first - dots[0].first) < (right.second - dots[0].second) * (left.first - dots[0].first);
    });
    s.push_back(0);
    s.push_back(1);
    int t = 1, idx = 2;
    while (idx < n) {
        int val = ccw(dots[s[t - 1]], dots[s[t]], dots[idx]);
        if (val > 0) {
            s.push_back(idx);
            idx++;
            t++;
        }
        else if (val == 0) {
            s.pop_back();
            s.push_back(idx);
            idx++;
        }
        else {
            s.pop_back();
            t--;
        }
    }
    printf("%d", (int)s.size());
    return 0;
}