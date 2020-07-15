// Problem No.: 18268
// Solver:      Jinmin Goh
// Date:        20200715
// URL: https://www.acmicpc.net/problem/18268

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

int main(){
    // parsing
    printf("Hello World!\n");
    int n, k;
    scanf("%d %d", &k, &n);
    vector< vector< int > > nums;
    vector< int > tempVec;
    nums.push_back(tempVec);
    for(int i = 0; i < k; i++){
        for(int j = 0; j < n; j++){
            int temp;
            scanf("%d", &temp);
            nums.back().push_back(temp);
        }
        vector< int > tempVec;
        nums.push_back(tempVec);
    }
    nums.pop_back();

    return 0;
}