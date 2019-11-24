// Problem No.: 10951
// Solver:      Jinmin Goh
// Date:        20191123
// URL: https://www.acmicpc.net/problem/10951

#include <iostream>
#include <list>
using namespace std;

int main()
{
    // this code makes input & output fast as scanf / printf
    // cin.tie(NULL);
    // ios_base::sync_with_stdio(false);
    // check following blog: https://starrykss.tistory.com/750

    int a, b;
    while(1)
    {
        cin >> a >> b;
        if(cin.eof()) return 0;
        cout << a + b << "\n";
    }

    return 0;
}