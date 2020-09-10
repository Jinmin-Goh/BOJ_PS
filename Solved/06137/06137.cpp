// Problem No.: 6137
// Solver:      Jinmin Goh
// Date:        20200909
// URL: https://www.acmicpc.net/problem/6137

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
    scanf("%d", &n);
    deque<char> charList;
    for(int i = 0; i < n; i++) {
        char temp;
        scanf("\n%c", &temp);
        charList.push_back(temp);
    }
    int cnt = 0;
    while(charList.size()) {
        char fchar = charList.front(), bchar = charList.back();
        if(fchar < bchar) {
            charList.pop_front();
            printf("%c", fchar);
        }
        else if(fchar > bchar) {
            charList.pop_back();
            printf("%c", bchar);
        }
        else {
            int p1 = 1, p2 = charList.size() - 2;
            while(p1 < p2 && charList[p1] == charList[p2]) {
                p1++;
                p2--;
            }
            if(charList[p1] < charList[p2]) {
                charList.pop_front();
                printf("%c", fchar);
            }
            else {
                charList.pop_back();
                printf("%c", bchar);
            }
        }
        cnt++;
        if(cnt == 80) {
            printf("\n");
            cnt = 0;
        }

    }
    return 0;
}