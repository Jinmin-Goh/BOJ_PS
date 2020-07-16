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
    int n, k, nums[11][21];
    scanf("%d %d", &k, &n);
    for(int i = 0; i < k; i++){
        for(int j = 0; j < n; j++){
            scanf("%d", &nums[i][j]);
        }
    }
    
    // same with below; different data structure
    // vector< vector< int > > nums;
    // vector< int > tempVec;
    // nums.push_back(tempVec);
    // for(int i = 0; i < k; i++){
    //     for(int j = 0; j < n; j++){
    //         int temp;
    //         scanf("%d", &temp);
    //         nums.back().push_back(temp);
    //     }
    //     vector< int > tempVec;
    //     nums.push_back(tempVec);
    // }
    // nums.pop_back();
    

    // overall time complexity is O(N^2*K)
    vector< pair< int, int > > ans;
    int check[21][21] = {};
    for(int p = 0; p < k; p++){
        for(int i = 0; i < n - 1; i++){
            for(int j = i + 1; j < n; j++){
                check[nums[p][j]][nums[p][i]] += 1;
                if(check[nums[p][j]][nums[p][i]] == k){
                    pair< int, int > temp(nums[p][j], nums[p][i]);
                    ans.push_back(temp);
                }
            }
        }
    }
    printf("%d", ans.size());
    return 0;
}