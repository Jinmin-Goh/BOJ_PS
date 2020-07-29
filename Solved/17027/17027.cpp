// Problem No.: 17027
// Solver:      Jinmin Goh
// Date:        20200728
// URL: https://www.acmicpc.net/problem/17027

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
    int nums[3][3] = {}, score[3] = {}, n;
    scanf("%d", &n);
    for(int i = 0; i < 3; i++) {
        nums[i][i] = 1;
    }
    for(int i = 0; i < n; i++) {
        int a, b, g;
        scanf("%d %d %d", &a, &b, &g);
        for(int i = 0; i < 3; i++) {
            swap(nums[i][a - 1], nums[i][b - 1]);
            if(nums[i][g - 1]) {
                score[i]++;
            }
        }   
    }
    int maxVal = 0;
    for(int i = 0; i < 3; i++) {
        maxVal = max(maxVal, score[i]);
    }
    
    printf("%d", maxVal);
    return 0;
}