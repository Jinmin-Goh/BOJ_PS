// Problem No.: 17200
// Solver:      Jinmin Goh
// Date:        20200728
// URL: https://www.acmicpc.net/problem/17200

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

struct cmp_str
{
   bool operator()(char const *a, char const *b) const
   {
      return strcmp(a, b) < 0;
   }
};

int main() {
    int n;
    scanf("%d", &n);
    map<string, vector<int>> skillmap;
    vector<vector<int>> graph(30);
    for(int i = 0; i < n; i++) {
        int k;
        scanf("%d", &k);
        for(int j = 0; j < k; j++) {
            char temp[25];
            scanf("%s", temp);
            string skill = temp;
            if(skillmap.find(skill) == skillmap.end()) {
                vector<int> temp(1, i);
                skillmap.insert(pair<string, vector<int>> (skill, temp));
            }
            else {
                skillmap[skill].push_back(i);
            }
        }
    }

    map<string, vector<int>>::iterator iter1, iter2;
    for(iter1 = skillmap.begin(); iter1 != skillmap.end(); iter1++) {
        map<string, vector<int>>::iterator tempIter = iter1;
        if(tempIter == skillmap.end()) {
            break;
        }
        tempIter++;
        for(iter2 = tempIter; iter2 != skillmap.end(); iter2++) {
            if(iter1->second.size() < iter2->second.size()) {
                swap(iter1, iter2);
            }
                
            bool inFlag = false;
            vector<int>::iterator temp1, temp2;
            for(temp1 = iter1->second.begin(); temp1 != iter1->second.end(); temp1++) {
                if(iter2->second.front() == *temp1) {
                    inFlag = true;
                    break;
                }
            }
            
            bool checkFlag = false;
            for(temp2 = iter2->second.begin(); temp2!= iter2->second.end(); temp2++) {
                checkFlag = false;
                for(temp1 = iter1->second.begin(); temp1 != iter1->second.end(); temp1++) {
                    if(*temp1 == *temp2) {
                        checkFlag = true;
                        break;
                    }
                }
                if(checkFlag) {
                    if(inFlag) {
                        continue;
                    }
                    else {
                        printf("no");
                        return 0;
                    }
                }
            }
            if((!inFlag && checkFlag) || (inFlag && !checkFlag)) {
                printf("no");
                return 0;
            }
        }
    }
    printf("yes");
    return 0;
}