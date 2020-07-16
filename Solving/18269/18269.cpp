// Problem No.: 18269
// Solver:      Jinmin Goh
// Date:        20200716
// URL: https://www.acmicpc.net/problem/18269

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
    int n;
    scanf("%d", &n);
    char str[101];
    scanf("%s", str);

    int ans = (n + 1) / 2;
    // string checking part; NEED TO FIX
    while(ans > 1){
        bool flag = false;
        for(int i = 1; i <= n - ans; i++){
            int pointer = 0;
            while(pointer < ans && str[pointer] == str[pointer + i]){
                pointer++;
            }
            if(pointer == ans){
                flag = true;
                break;   
            }
        }
        if(!flag){
            break;
        }
        ans -= 1;
    }

    printf("%d", ans);
    return 0;
}