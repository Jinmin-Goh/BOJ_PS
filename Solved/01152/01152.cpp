// Problem No.: 01152
// Solver:      Jinmin Goh
// Date:        191121
// URL: https://www.acmicpc.net/problem/1152

#include <iostream>
#include <list>
using namespace std;

int main()
{
    // this code makes input & output fast as scanf / printf
    //cin.tie(NULL);
    //ios_base::sync_with_stdio(false);
    // check following blog: https://starrykss.tistory.com/750
    
    
    char a[1000000] = {};
    cin.getline(a, 1000000);
    bool initflag = false, charflag = false;
    int start = 0;
    while(1)
    {
        if(a[start] != ' ')
            break;
        start++;
    }
    int i = start, cnt = 0;
    while(a[i] != '\0')
    {
        if(a[i] != ' ' && charflag == false)
        {
            charflag = true;
            cnt++;
        }
        if(a[i] == ' ')
            charflag = false;
        i++;
    }
    cout << cnt;
    return 0;
}