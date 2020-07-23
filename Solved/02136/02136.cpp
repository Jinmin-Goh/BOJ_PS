// Problem No.: 2136
// Solver:      Jinmin Goh
// Date:        20200722
// URL: https://www.acmicpc.net/problem/2136

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
    int n, l;
    scanf("%d %d", &n, &l);
    vector<pair<int, int>> rightMoveNums, leftMoveNums, nums;
    for(int i = 0; i < n; i++) {
        int temp;
        scanf("%d", &temp);
        pair<int, int> tempPair(temp > 0? temp : -temp, i + 1);
        // positive; move to right
        if(temp > 0) {
            rightMoveNums.push_back(tempPair);
        }
        // negative; move to left
        else {
            leftMoveNums.push_back(tempPair);
        }
        nums.push_back(tempPair);
    }
    sort(rightMoveNums.begin(), rightMoveNums.end());
    sort(leftMoveNums.begin(), leftMoveNums.end());
    sort(nums.begin(), nums.end());
    if(leftMoveNums.size() > 0 && rightMoveNums.size() > 0) {
        if(leftMoveNums.back().first > l - rightMoveNums.front().first) {
            printf("%d %d", nums.at(leftMoveNums.size() - 1).second, leftMoveNums.back().first);
        }
        else {
            printf("%d %d", nums.at(leftMoveNums.size()).second, l - rightMoveNums.front().first);
        }
    }
    else if(leftMoveNums.size() > 0) {
        printf("%d %d", nums.back().second, leftMoveNums.back().first);
    }
    else {
        printf("%d %d", nums.front().second, l - rightMoveNums.front().first);
    }

    return 0;
}