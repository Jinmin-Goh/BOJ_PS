// Problem No.: 5465
// Solver:      Jinmin Goh
// Date:        20200804
// URL: https://www.acmicpc.net/problem/5465




/**
 * A binary search solution for IOI 2009 problem "mecho"
 *
 * This solution should score 100%
 *
 * Carl Hultquist, chultquist@gmail.com
 */

#include <iostream>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <utility>
#include <deque>

using namespace std;

#define MAX_N 2000

int cx[4] = {1, -1, 0, 0};
int cy[4] = {0, 0, 1, -1};

char mainMap[MAX_N][MAX_N];
bool reachable[MAX_N][MAX_N];

// The time that it takes the bees to reach any cell in the map
int beeDistance[MAX_N][MAX_N];

int n, s;
int dx, dy;
int mx, my;

/**
 * Tests if Mecho is able to reach his home after staying with
 * the honey for the given delay time.
 */
bool test(int delay)
{
    // Check if the bees catch Mecho whilst he is still with
    // the honey.
    if (delay * s >= beeDistance[mx][my])
        return false;

    // Initialise data structures -- at the beginning of the search,
    // Mecho has only reached the cell with the honey. Note that it
    // is possible for the bees to catch Mecho at the honey -- but
    // we checked for this case above, and so if we reach this point
    // we know that Mecho is safe with the honey after the given
    // delay.
    memset(reachable, 0, sizeof(reachable));
    deque<pair<int, pair<int, int> > > q;
    q.push_back(make_pair(delay * s, make_pair(mx, my)));
    reachable[mx][my] = true;

    // Now do the main loop to see what other cells Mecho can reach.
    while (!q.empty())
    {
        int distance = q.front().first;
        int x = q.front().second.first;
        int y = q.front().second.second;

        q.pop_front();

        // If Mecho has reached his home, then we are done.
        if (mainMap[x][y] == 'D')
            return true;

        // Check neighbouring cells
        for (int c = 0; c < 4; c++)
        {
            int nx = x + cx[c];
            int ny = y + cy[c];

            // Check that the cell is valid, that it is not a tree, and
            // that Mecho can get here before the bees.
            if (nx < 0 || nx >= n || ny < 0 || ny >= n || mainMap[nx][ny] == 'T' || (distance + 1) >= beeDistance[nx][ny] || reachable[nx][ny])
                continue;

            // All OK, so add it to the queue
            q.push_back(make_pair(distance + 1, make_pair(nx, ny)));
            reachable[nx][ny] = true;
        }
    }

    // If we reach here, then Mecho was unable to reach his home.
    return false;
}
int main(int argc, char **argv)
{
    // Read in the data
    cin >> n >> s;

    deque<pair<int, int> > bq;
    memset(beeDistance, -1, sizeof(beeDistance));

    for (int i = 0; i < n; i++)
    {
        cin >> ws;
        for (int j = 0; j < n; j++)
        {
            cin >> mainMap[i][j];
            if (mainMap[i][j] == 'H')
            {
                bq.push_back(make_pair(i, j));
                beeDistance[i][j] = 0;
            }
            else if (mainMap[i][j] == 'M')
            {
                mx = i;
                my = j;

                // Bees can travel through the location of the honey
                mainMap[i][j] = 'G';
            }
            else if (mainMap[i][j] == 'D')
            {
                dx = i;
                dy = j;
            }
        }
    }

    // Precompute the time that it takes the bees to reach any other
    // cell in the map.
    while (!bq.empty())
    {
        int x = bq.front().first;
        int y = bq.front().second;

        bq.pop_front();

        for (int c = 0; c < 4; c++)
        {
            int nx = x + cx[c];
            int ny = y + cy[c];

            if (nx < 0 || nx >= n || ny < 0 || ny >= n || mainMap[nx][ny] != 'G' || beeDistance[nx][ny] != -1)
                continue;

            beeDistance[nx][ny] = beeDistance[x][y] + s;
            bq.push_back(make_pair(nx, ny));
        }
    }

    // The bees can never enter Mecho's home, so set this to a large
    // sentinel value.
    beeDistance[dx][dy] = n * n * s;

    // Binary search to find the maximum delay time.
    int low = -1, high = 2 * n * n;
    while (high - low > 1)
    {
        int mid = (low + high) >> 1;
        if (test(mid))
            low = mid;
        else
            high = mid;
    }

    cout << low << endl;
    return 0;
}


/*
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
    int hi = 2000, lo = 0;
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

*/