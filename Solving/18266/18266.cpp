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

    vector<vector<int>> allCows, posCows, negCows;
    int posCnt = 0, weightSum = 0, negCnt = 0;
    
    for(int i = 1; i <= n; i++) {
        int w, x, d;
        vector<int> temp;
        scanf("%d %d %d", &w, &x, &d);
        temp.push_back(w);
        temp.push_back(x);
        temp.push_back(d);
        allCows.push_back(temp);
        weightSum += w;

        if(d > 0) {
            posCnt++;
            posCows.push_back(temp);
        }
        else {
            negCnt++;
            negCows.push_back(temp);
        }
    }

    sort(allCows.begin(), allCows.end());
    sort(posCows.begin(), posCows.end());
    sort(negCows.begin(), negCows.end(), greater<vector<int>>());

    // first, find target t
    // if right moving cows are p cows, p rightmost cows will reach at right barn after L - x_i time
    // simillary, n - p leftmost cows will reach at right barn after x_i time
    int tempSum = 0, t = 0, posTempCnt = 0, negTempCnt = 0;
    vector<vector<int>>::iterator posIter = posCows.begin(), negIter = negCows.begin();
    while(tempSum < (weightSum + 1) / 2) {
        if(posTempCnt < posCnt && negTempCnt < negCnt) {
            if(posCows[posTempCnt][1] < l - negCows[negTempCnt][1]) {
                tempSum += posCows[posTempCnt][0];
                t = posCows[posTempCnt][1];
                posTempCnt++;
                posIter++;
            }
            else {
                tempSum += negCows[negTempCnt][0];
                t = l - negCows[negTempCnt][1];
                negTempCnt++;
                negIter++;
            }
        }
        else if(posTempCnt < posCnt) {
            tempSum += posCows[posTempCnt][0];
            t = posCows[posTempCnt][1];
            posTempCnt++;
            posIter++;
        }
        else {
            tempSum += negCows[negTempCnt][0];
            t = l - negCows[negTempCnt][1];
            negTempCnt++;
            negIter++;
        }
    }
    
    

    return 0;
}