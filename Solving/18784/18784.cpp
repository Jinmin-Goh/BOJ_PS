// Problem No.: 18784
// Solver:      Jinmin Goh
// Date:        20200714
// URL: https://www.acmicpc.net/problem/18784

#include <iostream>
#include <cstdlib>
#include <list>
#include <array>
#include <atomic>
#include <algorithm>
#include <deque>
#include <iostream>
#include <iterator>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
#include <tuple>

using namespace std;

int main(){
    // this code makes input & output fast as scanf / printf
    // cin.tie(NULL);
    // ios_base::sync_with_stdio(false);
    // check following blog: https://starrykss.tistory.com/750

    vector<pair<int, int>> coordX, coordY;
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        int x, y;
        scanf("%d %d", &x, &y);
        coordX.push_back({ x, y });
        // same result with: coordX.emplace_back(x, y);
        // pair<int, int> = temp(x, y);
        // coordX.push_back(temp);
        coordY.push_back({ y, x });
    }
    sort(coordX.begin(), coordX.end());
    sort(coordY.begin(), coordY.end());
    
    return 0;
}