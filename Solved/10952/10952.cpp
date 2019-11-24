// Problem No.: 10952
// Solver:      Jinmin Goh
// Date:        191121
// URL: https://www.acmicpc.net/problem/10952

#include <iostream>
#include <list>
using namespace std;

int main()
{
    // this code makes input & output fast as scanf / printf
    //cin.tie(NULL);
    //ios_base::sync_with_stdio(false);
    // check following blog: https://starrykss.tistory.com/750
    
    
    int a = 1, b = 1;
    bool initflag = true;
    while(1)
    {
        std::cin >> a >> b;
        if(a == 0 && b == 0)
            break;
        else cout << a + b << "\n";
    }
    
    return 0;
}