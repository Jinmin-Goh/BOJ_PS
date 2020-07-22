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
    vector<pair<int, int>> rightMoveNums, leftMoveNums;
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
    }
    sort(rightMoveNums.begin(), rightMoveNums.end());
    sort(leftMoveNums.begin(), leftMoveNums.end());
    
    pair<int, int> tempRight = rightMoveNums.front(), tempLeft = leftMoveNums.back();
    // both direction moving ants
    if(rightMoveNums.size() > 0 && leftMoveNums.size() > 0) {
        // no meeting
        if(tempRight.first > tempLeft.first) {
            if(tempLeft.first > l - tempRight.first) {
                printf("%d %d", tempLeft.second, tempLeft.first);
            }
            else {
                printf("%d %d", tempRight.second, l - tempRight.first);
            }
        }
        // meeting occurs
        else {
            if(tempLeft.first > l - tempRight.first) {
                printf("%d %d", rightMoveNums.front().second, tempLeft.first);
            }
            else {
                printf("%d %d", leftMoveNums.back().second, l - tempRight.first);
            }
        }
    }
    // only right moving ants
    else if(rightMoveNums.size() > 0) {
        printf("%d %d", tempRight.second, l - tempRight.first);
    }
    // only left moving ants
    else {
        printf("%d %d", tempLeft.second, tempLeft.first);
    }
    
    return 0;
}