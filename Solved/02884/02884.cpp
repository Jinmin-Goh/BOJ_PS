// Problem No.: 02884
// Solver:      Jinmin Goh
// Date:        191120
// URL: https://www.acmicpc.net/problem/2884

#include <iostream>
using namespace std;

int main()
{
    int h, m;
    cin >> h >> m;
    if(m < 45)
    {
        if(h == 0)
        {
            cout << 23 << " " << m + 15;
        }
        else cout << h - 1 << " " << m + 15;
    }
    else cout << h << " " << m -45;

    return 0;
}