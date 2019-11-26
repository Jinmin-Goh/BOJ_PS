// Problem No.: 2577
// Solver:      Jinmin Goh
// Date:        20191127
// URL: https://www.acmicpc.net/problem/2577

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

    int a, b, c, num;
    cin >> a >> b >> c;
    num = a * b * c;

    int count[11] = {0};

    while(num != 0)
    {
        count[num % 10]++;
        num /= 10;
    }

    for(int i = 0; i < 10; i++)
        cout << count[i] << endl;

    return 0;
}