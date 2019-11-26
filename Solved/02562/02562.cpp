// Problem No.: 2562
// Solver:      Jinmin Goh
// Date:        20191125
// URL: https://www.acmicpc.net/problem/2562

#include <iostream>
#include <list>
using namespace std;

int main()
{
    // this code makes input & output fast as scanf / printf
    // cin.tie(NULL);
    // ios_base::sync_with_stdio(false);
    // check following blog: https://starrykss.tistory.com/750

    int num[10] = {};
    int max = 0, max_pos = 0;
    
    for(int i = 0; i < 9; i++)
    {
        cin >> num[i];
        if(num[i] > max)
        {
            max = num[i];
            max_pos = i + 1;
        }
    }
    cout << max << endl << max_pos;

    return 0;
}