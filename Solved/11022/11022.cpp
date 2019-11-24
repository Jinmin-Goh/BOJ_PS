// Problem No.: 11022
// Solver:      Jinmin Goh
// Date:        191121
// URL: https://www.acmicpc.net/problem/11022

#include <iostream>
using namespace std;

int main()
{
    // this code makes input & output fast as scanf / printf
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    // check following blog: https://starrykss.tistory.com/750
    
    int n, a, b;
    cin >> n;
    
    for(int i = 1; i <= n; i++)
    {
        cin >> a >> b;
        cout << "Case #" << i << ": ";
        cout << a << " + " << b << " = " << a + b << "\n";
    }
    return 0;
}