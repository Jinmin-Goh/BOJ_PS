// Problem No.: 15552
// Solver:      Jinmin Goh
// Date:        191121
// URL: https://www.acmicpc.net/problem/15552

#include <iostream>
using namespace std;

int main()
{
    int n, a, b;
    cin >> n;

    // this code makes input & output fast as scanf / printf
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    // check following blog: https://starrykss.tistory.com/750
    
    for(int i = 1; i <= n; i++)
    {
        cin >> a >> b;
        cout << a + b << "\n";
    }
    return 0;
}