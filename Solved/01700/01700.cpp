// Problem No.: 1700
// Solver:      Jinmin Goh
// Date:        20200818
// URL: https://www.acmicpc.net/problem/1700

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

int query[110], holes[110], machinePluggedStatus[110]; 

int main() {
    int n, K;
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> K;
    for(int i = 0; i < K; i++) {
        cin >> query[i];
    }
    int ans = 0;
    for(int i = 0; i < K; i++) {
        // check already plugged in
        bool flag = false;
        for(int j = 0; j < n; j++) {
            if(query[i] == holes[j]) { 
                flag = true;
                break;
            }
        }
        if(flag) {
            continue;
        }
        

        // check empty hole
        for(int j = 0; j < n; j++) {
            if(!holes[j]) {
                flag = true;
                holes[j] = query[i]; // hole is using
                break;
            }
        }
        if(flag) { 
            continue;
        }

        // find not using or last using machine
        int pos, machinePos = -1;
        for(int j = 0; j < n; j++) {
            int lastPos = 0;
            for(int k = i + 1; k < K; k++) {
                if(query[k] == holes[j]) {
                    break;
                }
                lastPos++;
            }
            if(lastPos > machinePos) {
                pos = j;
                machinePos = lastPos;
            }

        }
        ans++;
        holes[pos] = query[i];
        
    }
    printf("%d", ans);

    return 0;
}