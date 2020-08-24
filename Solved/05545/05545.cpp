// Problem No.: 2585
// Solver:      Jinmin Goh
// Date:        20200824
// URL: https://www.acmicpc.net/problem/2585

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

int topping[10010];

int main() {
    int n, a, b, dough;
    scanf("%d", &n);
    scanf("%d %d", &a, &b);
    scanf("%d", &dough);
    for(int i = 0; i < n; i++) {
        scanf("%d", &topping[i]);
    }

    int cost = 0, cal = 0;
    cal += dough;
    cost += a;
    double unit = (double)cal / cost;

    sort(topping, topping + n);
    for(int i = n - 1; i >= 0; i--) {
        int tempCost = cost + b, tempCal = cal + topping[i];
        if((double)tempCal / tempCost < (double)cal / cost) {
            break;
        }
        cost = tempCost;
        cal = tempCal;
    }

    printf("%d", cal / cost);

    return 0;
}