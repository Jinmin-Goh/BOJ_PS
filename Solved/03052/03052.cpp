// Problem No.: 3052
// Solver:      Jinmin Goh
// Date:        20191128
// URL: https://www.acmicpc.net/problem/3052

#include <iostream>
#include <list>
#include <stdlib.h>
using namespace std;

int main()
{
    // this code makes input & output fast as scanf / printf
    // cin.tie(NULL);
    // ios_base::sync_with_stdio(false);
    // check following blog: https://starrykss.tistory.com/750

    bool check[42] = {false};
    int sum = 0;
    for(int i = 0; i < 10; i++)
    {
        int temp;
        cin >> temp;
        check[temp % 42] = true;
    }
    for(int i = 0; i < 42; i++)
    {
        sum += check[i];
    }

    cout << sum;

    return 0;
}