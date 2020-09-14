// Problem No.: 19843
// Solver:      Jinmin Goh
// Date:        20200914
// URL: https://www.acmicpc.net/problem/19843

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

int main() {
    int t, n, sleep1, sleep2;
    map<string, int> days;
    days["Mon"] = 0;
    days["Tue"] = 1;
    days["Wed"] = 2;
    days["Thu"] = 3;
    days["Fri"] = 4;

    scanf("%d %d", &t, &n);
    string day1, day2;
    int temp = 0;
    for(int i = 0; i < n; i++) {
        cin >> day1 >> sleep1 >> day2 >> sleep2;
        temp += 24 * (days[day2] - days[day1]) + sleep2 - sleep1;
    }
    if(t - temp > 48) {
        printf("-1");
    }
    else if (t < temp) {
        printf("0");
    }
    else {
        printf("%d", t - temp);
    }
    return 0;
}