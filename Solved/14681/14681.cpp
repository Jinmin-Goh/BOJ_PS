// Problem No.: 14681
// Solver:      Jinmin Goh
// Date:        20201018
// URL: https://www.acmicpc.net/problem/14681

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
    int x, y;
    scanf("%d", &x);
    scanf("%d", &y);
    if(x > 0 && y > 0) {
        printf("1");
    }
    else if(x < 0 && y > 0) {
        printf("2");
    }
    else if(x < 0 && y < 0) {
        printf("3");
    }
    else {
        printf("4");
    }
    return 0;
}