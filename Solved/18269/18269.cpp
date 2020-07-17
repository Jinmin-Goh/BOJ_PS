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
    char str[101] = {};
    scanf("%s", str);

    int ans = n - 1;
    // string checking part; NEED TO FIX; add one more loop
    while(ans > 0){
        bool sameFlag = true;  // check substring is same
        for(int start = 0; start < n - ans; start++){
            // i is distance between two substrings
            for(int i = start + 1; i <= n - ans; i++){
                int p = 0;
                while(p < ans && str[start + p] == str[p + i]){
                    p++;
                }
                if(p != ans){   // same substring
                    sameFlag = false;   
                }
                else{           // different substring
                    sameFlag = true;   
                }
                // if two substring is same; found minimum value, break
                if(sameFlag){
                    break;
                }
            }
            if(sameFlag){
                break;
            }
        }
        if(sameFlag){
            break;
        }
        ans -= 1;
    }

    printf("%d", ans + 1);
    return 0;
}
