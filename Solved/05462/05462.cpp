// Problem No.: 5462
// Solver:      Jinmin Goh
// Date:        20200804
// URL: https://www.acmicpc.net/problem/5462

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

int solvedTable[2010][2010], score[2010], solvedCntList[2010];

int main() {
    int n, t, p, place = 1;
    scanf("%d %d %d", &n, &t, &p);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < t; j++) {
            scanf("%d", &solvedTable[i][j]);
        }
    }
    for(int i = 0; i < t; i++) {
        int notSolvedCnt = 0;
        for(int j = 0; j < n; j++) {
            if(!solvedTable[j][i]) {
                notSolvedCnt++;
            }
        }
        for(int j = 0; j < n; j++) {
            if(solvedTable[j][i]) {
                score[j] += notSolvedCnt;
                solvedCntList[j]++;
            }
        }
    }

    for(int i = 0; i < p - 1; i++) {
        if(score[i] > score[p - 1] || (score[i] == score[p - 1] && solvedCntList[i] >= solvedCntList[p - 1])) {
            place++;
        }
    }

    for(int i = p; i < n; i++) {
        if(score[i] > score[p - 1] || (score[i] == score[p - 1] && solvedCntList[i] > solvedCntList[p - 1])) {
            place++;
        }
    }

    printf("%d %d", score[p - 1], place);

    return 0;
}