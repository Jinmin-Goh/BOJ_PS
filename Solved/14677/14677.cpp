// Problem No.: 14677
// Solver:      Jinmin Goh
// Date:        20200909
// URL: https://www.acmicpc.net/problem/14677

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


int dpTable[1510][1510];
char drug[1510], flag[4] = "BLD";

int dpFunc(int curr, int front, int back) {
    if(front > back) {
        return 0;
    }
    if(dpTable[front][back] == -1) {
        int tempVal = 0;
        if(drug[front] == flag[curr]) {
            tempVal = max(tempVal, dpFunc((curr + 1) % 3, front + 1, back) + 1);
        }
        if(drug[back] == flag[curr]) {
            tempVal = max(tempVal, dpFunc((curr + 1) % 3, front, back - 1) + 1);
        }
        dpTable[front][back] = tempVal;
    }

    return dpTable[front][back];
}

int main() {
    int n;
    scanf("%d", &n);
    scanf("%s", drug);
    for(int i = 0; i < 3 * n; i++) {
        for(int j = 0; j < 3 * n; j++) {
            dpTable[i][j] = -1;
        }
    }
    dpFunc(0, 0, 3 * n - 1);
    printf("%d", dpTable[0][3 * n - 1]);
    return 0;
}