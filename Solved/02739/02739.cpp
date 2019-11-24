// Problem No.: 02739
// Solver:      Jinmin Goh
// Date:        191120
// URL: https://www.acmicpc.net/problem/2739

#include <iostream>
using namespace std;

int main()
{
    int a;
    cin >> a;
    for(int i = 1; i < 10; i++)
    {
        cout << a << " * " << i << " = " << a * i << "\n";
    }
    return 0;
}