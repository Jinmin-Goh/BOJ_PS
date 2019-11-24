// Problem No.: 01330
// Solver:      Jinmin Goh
// Date:        191120
// URL: https://www.acmicpc.net/problem/1330

#include <iostream>

using namespace std;

int main()
{
    int a, b;
    
    cin >> a >> b;
    if(a > b)
        cout << ">";
    else if(a == b)
        cout << "==";
    else
        cout << "<";

    return 0;
}