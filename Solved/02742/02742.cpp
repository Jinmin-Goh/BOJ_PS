// Problem No.: 02742
// Solver:      Jinmin Goh
// Date:        191121
// URL: https://www.acmicpc.net/problem/2742

#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    // this code makes input & output fast as scanf / printf
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    // check following blog: https://starrykss.tistory.com/750
    
    for(int i = n; i >= 1; i--)
    {
        cout << i << "\n";
    }
    return 0;
}