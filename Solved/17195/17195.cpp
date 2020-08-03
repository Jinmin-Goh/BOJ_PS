// Problem No.: 17195
// Solver:      Jinmin Goh
// Date:        20200803
// URL: https://www.acmicpc.net/problem/17195

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
    int n;
    int table[1010][1010] = {};
    scanf("%d", &n);
    
    for(int i = 0; i < n; i++) {
        char temp[1010] = {};
        scanf("%s", temp);
        for(int j = 0; j < n; j++) {
            table[i][j] = temp[j] == 'L';
        }
    }
    
    for(int i = 0; i < n; i++) {
        if(table[0][i] == 1) {
            for(int j = 0; j < n; j++) {
                table[j][i] ^= 1;
            }
        }
    }
    for(int i = 1; i < n; i++) {
        if(table[i][0] == 1) {
            for(int j = 0; j < n; j++) {
                table[i][j] ^= 1;
            }
        }
    }

    int oneCnt = 0;
    for(int i = 1; i < n; i++) {
        for(int j = 1; j < n; j++) {
            if(table[i][j] == 1) {
                oneCnt++;
            }
        }
    }
    if(oneCnt == (n - 1) * (n - 1)) {
        printf("1 1");
        return 0;
    }
    else if(oneCnt == n - 1) {
        for(int i = 1; i < n; i++)
        {
            if(table[1][i] == 1) {
                int temp = 0;
                for(int j = 1; j < n; j++) {
                    if(table[j][i] == 1) {
                        temp++;
                    }
                }
                if(temp == n - 1) {
                    printf("%d %d", 1, i + 1);
                    return 0;
                }
            }
        }
        for(int i = 1; i < n; i++)
        {
            if(table[i][1] == 1) {
                int temp = 0;
                for(int j = 1; j < n; j++) {
                    if(table[i][j] == 1) {
                        temp++;
                    }
                }
                if(temp == n - 1) {
                    printf("%d %d", i + 1, 1);
                    return 0;
                }
            }
        }
        printf("-1");
    }
    else if(oneCnt == 1) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if(table[i][j] == 1) {
                    printf("%d %d", i + 1, j + 1);
                    return 0;
                }
            }
        }
    }
    printf("-1");

    return 0;
}