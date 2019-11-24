// Problem No.: 10817
// Solver:      Jinmin Goh
// Date:        191120
// URL: https://www.acmicpc.net/problem/10817

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int a[3];
    cin >> a[0] >> a[1] >> a[2];
    sort(a, a + 3);
    cout << a[1];
    return 0;
}