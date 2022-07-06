// Problem No.: 25317
// Solver:      Jinmin Goh
// Date:        20220706
// URL: https://www.acmicpc.net/problem/25317

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

typedef long long int lli;

int arr[800010];
lli query[200010][3];

void update(int idx, int val, int node, int l, int r) {
    if (idx <= l && r <= idx) {
        arr[node] = val;
        return;
    }
    else if (idx < l || r < idx) {
        return;
    }
    int m = (l + r) / 2;
    update(idx, val, node * 2, l, m);
    update(idx, val, node * 2 + 1, m + 1, r);
    arr[node] = arr[node * 2] + arr[node * 2 + 1];
    return;
}

int print_sum(int ql, int qr, int node, int l, int r) {
    if (ql <= l && r <= qr) {
        return arr[node];
    }
    else if (qr < l || r < ql) {
        return 0;
    }
    int m = (l + r) / 2;
    int l_val = print_sum(ql, qr, node * 2, l, m);
    int r_val = print_sum(ql, qr, node * 2 + 1, m + 1, r);
    return l_val + r_val;
}

struct HashFunction {
    const std::size_t operator()(const tuple<lli, lli> &x) const {
        return get<0>(x) ^ get<1>(x);
    }
};

int main() {
    lli n;
    bool plus = true, zero = false;
    set<lli> zero_set;
    vector< tuple< lli, tuple< lli, lli > > > nums;
    scanf("%lld", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &query[i][0]);
        if (query[i][0] == 1) {
            scanf("%lld %lld", &query[i][1], &query[i][2]);
            if (query[i][1] != 0) {
                lli a = query[i][1], b = query[i][2];
                tuple< lli, lli > second(a, b);
                lli m = -b / a;
                if (b % a == 0) {
                    tuple< lli, tuple< lli, lli > > first(2 * m, second);
                    nums.push_back(first);
                }
                else {
                    if ((a > 0 && -b < 0) || (-b > 0 && a < 0)) {
                        m--;
                    }
                    tuple< lli, tuple< lli, lli > > first(2 * m + 1, second);
                    nums.push_back(first);
                }
            }
        }
        else {
            scanf("%lld", &query[i][1]);
            tuple< lli, lli > second(1, -query[i][1]);
            tuple< lli, tuple< lli, lli > > first(2 * query[i][1], second);
            nums.push_back(first);
        }
    }
    sort(nums.begin(), nums.end());
    
    unordered_map< tuple< lli, lli >, int, HashFunction > nums_pos;
    for (int i = 0; i < nums.size(); i++) {
        nums_pos.insert({get<1>(nums[i]), i + 1});
    }
    for (int i = 0; i < n; i++) {
        if (query[i][0] == 1) {
            lli a = query[i][1], b = query[i][2];
            if (a == 0 && b == 0) {
                zero = true;
                continue;
            }
            else if (a == 0) {
                if (b < 0) {
                    plus = !plus;
                }
                continue;
            }
            if (a < 0) {
                plus = !plus;
            }
            if (b % a == 0) {
                zero_set.insert(-b / a);
            }
            tuple< lli, lli > temp(a, b);
            const int &nums_pos_temp = nums_pos[temp];
            lli val = print_sum(nums_pos_temp, nums_pos_temp, 1, 1, nums.size());
            update(nums_pos_temp, val + 1, 1, 1, nums.size());
        }
        else {
            if (zero) {
                printf("0\n");
                continue;
            }
            if (zero_set.find(query[i][1]) != zero_set.end()) {
                printf("0\n");
            }
            else {
                tuple< lli, lli > temp(1, -query[i][1]);
                lli val = print_sum(nums_pos[temp], nums.size(), 1, 1, nums.size());
                if (!plus) {
                    val++;
                }
                if (val % 2) {
                    printf("-\n");
                }
                else {
                    printf("+\n");
                }
            }
        }
    }
    return 0;
}