// Problem No.: 08393
// Solver:      Jinmin Goh
// Date:        191121
// URL: https://www.acmicpc.net/problem/8393

#include <iostream>
using namespace std;

int main()
{
    int n, sum = 0;
    cin >> n;
    for(int i = 1; i <= n; i++)
    {
        sum = sum + i;
    }

    cout << sum;
    return 0;
}