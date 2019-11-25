// Problem No.: 10818
// Solver:      Jinmin Goh
// Date:        20191125
// URL: https://www.acmicpc.net/problem/10818

#include <iostream>
#include <list>
using namespace std;

int main()
{
    // this code makes input & output fast as scanf / printf
    // cin.tie(NULL);
    // ios_base::sync_with_stdio(false);
    // check following blog: https://starrykss.tistory.com/750

    int a;
    cin >> a;
    int num[a + 1] = {};
    for(int i = 0; i < a; i++)
    {
        cin >> num[i];
    }
    int min = 1000000, max = -1000000;
    for(int i = 0; i < a; i++)
    {
        if(num[i] < min)
            min = num[i];
        if(num[i] > max)
            max = num[i];
    }
    cout << min << " " << max << endl;

    return 0;
}