// Problem No.: 13701
// Solver:      Jinmin Goh
// Date:        20200818
// URL: https://www.acmicpc.net/problem/13701

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

int nums[1 + (1 << 20)];

// use int but divide into 32 bits to check visited

int main() {
    int n = 0, temp;
    while(scanf("%d", &temp) == 1) {
        int a = temp / 32, b = temp % 32;

        if(nums[a] & (1 << b)) {
            continue;
        }
        printf("%d ", temp);
        nums[a] += (1 << b);
    }

    return 0;
}