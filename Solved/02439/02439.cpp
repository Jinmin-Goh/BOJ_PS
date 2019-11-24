// Problem No.: 02439
// Solver:      Jinmin Goh
// Date:        191121
// URL: https://www.acmicpc.net/problem/2439

#include <iostream>
using namespace std;

int main()
{
    // this code makes input & output fast as scanf / printf
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    // check following blog: https://starrykss.tistory.com/750
    
    int n;
    cin >> n;
    
    for(int i = 1; i <= n; i++)
    {
        for(int j = 1; j <= n - i; j++)
            cout << " ";
        for(int j = n - i + 1; j <= n; j++)
            cout << "*";
        cout << "\n";
    }
    return 0;
}