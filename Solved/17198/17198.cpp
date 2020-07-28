// Problem No.: 17198
// Solver:      Jinmin Goh
// Date:        20200726
// URL: https://www.acmicpc.net/problem/17198

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
    char mapTable[15][15] = {};
    for(int i = 0; i < 10; i++) {
        scanf("%s", mapTable[i]);
    }
    pair<int, int> barn, lake, rock;
    for(int i = 0; i < 10; i++) {
        for(int j = 0; j < 10; j++) {
            if(mapTable[i][j] == 'L') {
                lake.first = i;
                lake.second = j;
            }
            if(mapTable[i][j] == 'B') {
                barn.first = i;
                barn.second = j;
            }
            if(mapTable[i][j] == 'R') {
                rock.first = i;
                rock.second = j;
            }
            
        }
    }
    if(lake.first == barn.first && barn.first == rock.first && ((lake.second > rock.second && rock.second > barn.second) || (lake.second < rock.second && rock.second < barn.second))) {
        printf("%d", abs(lake.second - barn.second) + 1);
    }
    else if(lake.second == barn.second && barn.second == rock.second && ((lake.first > rock.first && rock.first > barn.first) || (lake.first < rock.first && rock.first < barn.first))) {
        printf("%d", abs(lake.first - barn.first) + 1);
    }
    else {
        printf("%d", abs(lake.first - barn.first) + abs(lake.second - barn.second) - 1);
    }
    return 0;
}