// Problem No.: 1110
// Solver:      Jinmin Goh
// Date:        20191123
// URL: https://www.acmicpc.net/problem/1110

#include <iostream>
#include <list>
using namespace std;

int main()
{
    // this code makes input & output fast as scanf / printf
    // cin.tie(NULL);
    // ios_base::sync_with_stdio(false);
    // check following blog: https://starrykss.tistory.com/750

    int a, cnt = 0, temp1 = 0, temp2 = 0;
    cin >> a;
    temp2 = a;
    while(1)
    {    
        cnt++;
        temp1 = temp2 / 10 + temp2 % 10;
        temp1 = (temp2 % 10) * 10 + temp1 % 10;
        if(temp1 == a) break;
        temp2 = temp1;
    }
    cout << cnt;

    return 0;
}