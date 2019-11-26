// Problem No.: 2920
// Solver:      Jinmin Goh
// Date:        20191126
// URL: https://www.acmicpc.net/problem/2920

#include <iostream>
#include <list>
using namespace std;

int main()
{
    // this code makes input & output fast as scanf / printf
    // cin.tie(NULL);
    // ios_base::sync_with_stdio(false);
    // check following blog: https://starrykss.tistory.com/750

    int num[9] = {};
    bool ascFlag = true, desFlag = true;
    for(int i = 0; i < 8; i++)
    {
        cin >> num[i];
    }
    for(int i = 1; i < 8; i++)
    {
        if(num[i] >= num[i-1])
            desFlag = false;
        if(num[i] <= num[i-1])
            ascFlag = false;
    }
    if(ascFlag)
        cout << "ascending";
    if(desFlag)
        cout << "descending";
    if(!ascFlag && !desFlag)
        cout << "mixed";

    return 0;
}