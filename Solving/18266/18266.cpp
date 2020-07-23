// Problem No.: 18266
// Solver:      Jinmin Goh
// Date:        20200722
// URL: https://www.acmicpc.net/problem/18266

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

    int allCows[60000][3] = {}, posCows[60000][3] = {}, negCows[60000][3] = {}, posCnt = 0, negCnt = 0;
    
    for(int i = 1; i <= n; i++) {
        int w, x, d;
        scanf("%d %d %d", &w, &x, &d);
        allCows[i][0] = w;
        allCows[i][1] = x;
        allCows[i][2] = d;
        
        if(d > 0) {
            posCnt++;
            posCows[posCnt][0] = w;
            posCows[posCnt][1] = x;
            posCows[posCnt][2] = d;
        }
        else {
            negCnt++;
            negCows[negCnt][0] = w;
            negCows[negCnt][1] = x;
            negCows[negCnt][2] = d;
        }
    }

    sort(allCows, allCows + n);
    sort(posCows, posCows + posCnt);
    sort(negCows, negCows + negCnt);
    

    return 0;
}