// Problem No.: 10950
// Solver:      Jinmin Goh
// Date:        191120
// URL: https://www.acmicpc.net/problem/10950

#include <iostream>
using namespace std;

int main()
{
    int n, a, b;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> a >> b;
        cout << a + b << "\n";
    }
    return 0;
}