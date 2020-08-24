// Problem No.: 9935
// Solver:      Jinmin Goh
// Date:        20200824
// URL: https://www.acmicpc.net/problem/9935

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

char stringList[1000010], explode[40], result[1000010];

int main() {
    scanf("%s", stringList);
    scanf("%s", explode);
    string _stringList = (string) stringList, _explode = (string) explode;
    int stringLen = _stringList.size(), explodeLen = _explode.size();

    map<int, int> jumpTable;
    bool flag = false;
    int pointer = 0;
    for(int i = 0; i < stringLen; i++) {
        result[pointer] = stringList[i];
        if(stringList[i] == explode[explodeLen - 1]) {
            int j;
            for(j = 0; j < explodeLen; j++) {
                if(result[pointer - j] != explode[explodeLen - 1 - j]) {
                    break;
                }
            }
            if(j == explodeLen) {
                pointer -= explodeLen;
            }
        }
        pointer++;
    }

    if(pointer == 0) {
        printf("FRULA");
        return 0;
    }

    for(int i = 0; i < pointer; i++) {
        printf("%c", result[i]);
    }

    return 0;
}