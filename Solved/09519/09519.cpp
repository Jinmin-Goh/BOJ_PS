// Problem No.: 9519
// Solver:      Jinmin Goh
// Date:        20200824
// URL: https://www.acmicpc.net/problem/9519

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

vector<string> words;

int main() {
    int n, length;
    scanf("%d", &n);
    char temp[1010];
    scanf("%s", temp);
    string temp2 = (string) temp;
    words.push_back(temp2);
    length = temp2.size();
    if(length <= 1) {
        printf("%s", temp);
        return 0;
    }
    int cnt = 1;
    char before[1010], after[1010];
    words[0].copy(before, length);
    while(true) {
        if(length % 2) {
            after[length - 1] = before[length / 2];
        }
        for(int i = 0; i < length / 2; i++) {
            after[2 * i] = before[i];
            after[2 * i + 1] = before[length - 1 - i];
        }
        if((string) after == words[0]) {
            break;
        }

        for(int i = 0; i < length; i++) {
            before[i] = after[i];
        }

        //words.push_back((string) after);
        //printf("%s\n", after);
        cnt++;
    }
    n %= cnt;

    if(n == 0) {
        printf("%s", words[0].c_str());
    }
    else {
        char before[1010], after[1010];
        words[0].copy(before, length);  
        for(int i = 0; i < cnt - n; i++) {
            if(length % 2) {
                after[length - 1] = before[length / 2];
            }
            for(int i = 0; i < length / 2; i++) {
                after[2 * i] = before[i];
                after[2 * i + 1] = before[length - 1 - i];
            }
            if((string) after == words[0]) {
                break;
            }

            for(int i = 0; i < length; i++) {
                before[i] = after[i];
            }

            //words.push_back((string) after);
            //printf("after: %s\n", after);
        }
        printf("%s", before);
    }

    return 0;
}