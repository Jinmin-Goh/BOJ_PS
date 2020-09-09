// Problem No.: 14715
// Solver:      Jinmin Goh
// Date:        20200907
// URL: https://www.acmicpc.net/problem/14715

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

bool tempList[1000001];
int main() {
    tempList[0] = true;
    tempList[1] = true;
    vector<int>prime;
    for(int i = 2; i <= 1000000; i++) {
        if(!tempList[i]) {
            prime.push_back(i);
            int cnt = 2 * i;
            while(cnt <= 1000000) {
                tempList[cnt] = true;
                cnt += i;
            }
        }
    }

    int n, cnt = 0;
    scanf("%d", &n);
    for(int i = 0; i < prime.size(); i++) {
        if(n == 1) {
            break;
        }
        while(!(n % prime[i])) {
            n /= prime[i];
            cnt++;
        }
    }
    int ans = 0;
    cnt -= 1;
    while(cnt > 0) {
        ans++;
        cnt >>= 1;
    }

    printf("%d", ans);
    return 0;
}