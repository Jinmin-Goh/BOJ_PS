// Problem No.: 19532
// Solver:      Jinmin Goh
// Date:        20200807
// URL: https://www.acmicpc.net/problem/19532

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
    int a, b, c, d, e, f;
    scanf("%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f);
    printf("%d %d", (c * e - b * f) / (a * e - b * d), (c * d - a * f) / (b * d - a * e));
    return 0;
}