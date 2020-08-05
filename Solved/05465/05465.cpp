// Problem No.: 5465
// Solver:      Jinmin Goh
// Date:        20200804
// URL: https://www.acmicpc.net/problem/5465


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

char table[810][810];
int hornetDistance[810][810], visited[810][810];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int main() {
    int n, s;
    pair<int, int> bear, home;
    vector<pair<int, int>> hornet;
    scanf("%d %d", &n, &s);
    for(int i = 0; i < n; i++) {
        scanf("%s", table[i]);
    }
    
    vector<pair<int, int>>::iterator iter;
    for(int i = 0; i < 810; i++) {
        for(int j = 0; j < 810; j++) {
            hornetDistance[i][j] = 1e9;
        }
    }
    
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if(table[i][j] == 'M') {
                bear.first = i;
                bear.second = j;
            }
            if(table[i][j] == 'D') {
                home.first = i;
                home.second = j;
            }
            if(table[i][j] == 'H') {
                pair<int, int> temp;
                temp.first = i;
                temp.second = j;
                hornetDistance[i][j] = 0;
                hornet.push_back(temp);
            }
        }
    }
    
    queue<pair<int, int>> stackList_temp;
    for(iter = hornet.begin(); iter != hornet.end(); iter++) {
        for(int i = 0; i < 810; i++) {
            for(int j = 0; j < 810; j++) {
                visited[i][j] = 0;
            }
        }
        stackList_temp.push(*iter);
    }

    int cnt = 0;
    while(stackList_temp.size() > 0) {
        stackList_temp.push(pair<int, int> (-1, -1));
        while(true) {   
            pair<int, int> temp = stackList_temp.front();
            stackList_temp.pop();
            int x = temp.first, y = temp.second;
            if(x == -1 && y == -1) {
                break;
            }
            if(visited[x][y] || table[x][y] == 'T' || table[x][y] == 'D') {
                continue;
            }
            visited[x][y] = 1;
            //printf("%d %d\n", x, y);
            hornetDistance[x][y] = min(hornetDistance[x][y], cnt);
            for(int i = 0; i < 4; i++) {
                if(x + dx[i] >= 0 && x + dx[i] < n && y + dy[i] < n && y + dy[i] >= 0 && !visited[x + dx[i]][y + dy[i]]) {
                    //printf("add: %d %d\n", x + dx[i], y + dy[i]);
                    stackList_temp.push(pair<int, int> (x + dx[i], y + dy[i]));
                }
            }
        }
        cnt += s;
    }

    // initial check

    for(int i = 0; i < 810; i++) {
        for(int j = 0; j < 810; j++) {
            visited[i][j] = 0;
        }
    }
    bool flag = false;
    cnt = 0;
    queue<pair<int, int>> stackList;
    stackList.push(bear);
    while(stackList.size() > 0) {
        stackList.push(pair<int, int> (-1, -1));
        while(true) {
            pair<int, int> temp = stackList.front();
            stackList.pop();
            int x = temp.first, y = temp.second;
            if(x == -1 && y == -1) {
                break;
            }
            if(visited[x][y] || table[x][y] == 'T' || hornetDistance[x][y] <= cnt) {
                continue;
            }
            if(table[x][y] == 'D') {
                flag = true;
                break;
            }
            visited[x][y] = 1;
            for(int i = 0; i < 4; i++) {
                if(x + dx[i] >= 0 && x + dx[i] < n && y + dy[i] < n && y + dy[i] >= 0 && !visited[x + dx[i]][y + dy[i]]) {
                    stackList.push(pair<int, int> (x + dx[i], y + dy[i]));
                }
            }
        }
        if(flag) {
            break;
        }
        cnt++;
    }
    if(!flag) {
        printf("-1");
        return 0;
    }


    // binary search
    int hi = 1e6, lo = 0;
    while(lo < hi) {
        int mid = (hi + lo + 1) / 2;

        for(int i = 0; i < 810; i++) {
            for(int j = 0; j < 810; j++) {
                visited[i][j] = 0;
            }
        }
        bool flag = false;
        int cnt = mid * s;
        queue<pair<int, int>> stackList;
        stackList.push(bear);
        while(stackList.size() > 0) {
            stackList.push(pair<int, int> (-1, -1));
            while(true) {
                pair<int, int> temp = stackList.front();
                stackList.pop();
                int x = temp.first, y = temp.second;
                if(x == -1 && y == -1) {
                    break;
                }
                if(visited[x][y] || table[x][y] == 'T' || hornetDistance[x][y] <= cnt) {
                    continue;
                }
                if(table[x][y] == 'D') {
                    flag = true;
                    break;
                }
                visited[x][y] = 1;
                for(int i = 0; i < 4; i++) {
                    if(x + dx[i] >= 0 && x + dx[i] < n && y + dy[i] < n && y + dy[i] >= 0 && !visited[x + dx[i]][y + dy[i]]) {
                        stackList.push(pair<int, int> (x + dx[i], y + dy[i]));
                    }
                }
            }
            if(flag) {
                break;
            }
            cnt++;
        }
        if(flag) {
            lo = mid;
        }
        else {
            hi = mid - 1;
        }
    }
    
    printf("%d", hi);
    return 0;
}