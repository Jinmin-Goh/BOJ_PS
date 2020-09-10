// Problem No.: 2011
// Solver:      Jinmin Goh
// Date:        20200909
// URL: https://www.acmicpc.net/problem/2011

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

char charList[5010];
int dpList[5010];

int main() {
    scanf("%s", charList + 1);
    charList[0] = ' ';
    dpList[0] = 1;
    
    for(int i = 1; i < strlen(charList); i++) {
        if(charList[i] - '0' != 0) {
            dpList[i] += dpList[i - 1];
        }
        
        int temp = (charList[i - 1] - '0') * 10 + charList[i] - '0';
        if(temp >= 10 && temp <= 26) {
            dpList[i] += dpList[i - 2];
        }

        dpList[i] %= 1000000;
    }
    printf("%d", dpList[strlen(charList) - 1] % 1000000);
    return 0;
}