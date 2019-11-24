// Problem No.: 02753
// Solver:      Jinmin Goh
// Date:        191120
// URL: https://www.acmicpc.net/problem/2753

#include <iostream>
using namespace std;

int main()
{
    int a;
    cin >> a;
    if(a % 4 == 0)
    {
        if(a % 100 == 0)
        {
            if(a % 400 == 0)
                printf("1");
            else
                printf("0");
        }
        else printf("1");
    }
    else printf("0");
    return 0;
}