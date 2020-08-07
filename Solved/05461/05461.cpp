// Problem No.: 5461
// Solver:      Jinmin Goh
// Date:        20200804
// URL: https://www.acmicpc.net/problem/5461

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

int s[500010], q[500010];
bool usedCandidate[500010];
pair<double, int> ratio[500010];

int main() {
    int n;
    double w;
    scanf("%d %lf", &n, &w);
    for(int i = 1; i <= n; i++) {
        scanf("%d %d", &s[i], &q[i]);
        ratio[i] = pair<double, int> ((double)s[i] / q[i], i);
    }
    sort(ratio + 1, ratio + n + 1);
    
    double totalQ = 0, bestCost = 0, currCost = 0;
    int bestIndex = 0, bestNums = 0;;
    priority_queue<double> members;
    for(int i = 1; i <= n; i++) {
        members.push(q[ratio[i].second]);
        totalQ += q[ratio[i].second];

        double qMax = w / ratio[i].first;   // quality that can get maximum
        while(totalQ > qMax) {
            totalQ -= members.top();
            members.pop();
        }
        
        int num = members.size();
        currCost = totalQ * ratio[i].first;
        if(num > bestNums || (num == bestNums && currCost < bestCost)) {
            bestNums = num;
            bestCost = currCost;
            bestIndex = i;
        }
    }


    priority_queue<pair<double, int> > heap;
    totalQ = 0;
    for (int i = 0; i <= bestIndex; i++)
    {
        heap.push(make_pair(q[ratio[i].second], ratio[i].second));
        totalQ += q[ratio[i].second];
        usedCandidate[ratio[i].second] = true;
    }

    double maxQual = w / ratio[bestIndex].first;
    while (totalQ > maxQual)
    {
        totalQ -= heap.top().first;
        usedCandidate[heap.top().second] = false;
        heap.pop();
    }

    printf("%d\n", bestNums);
    for (int i = 1; i <= n; i++)
        if (usedCandidate[i])
            printf("%d\n", i);

    return 0;
}