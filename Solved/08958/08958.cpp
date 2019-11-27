// Problem No.: 8958
// Solver:      Jinmin Goh
// Date:        20191128
// URL: https://www.acmicpc.net/problem/8958

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

    int n, count = 0, sum = 0;
    cin >> n;
    char result[81] = {};

    for(int i = 0; i < n; i++)
    {
        *result = {};
        cin >> result;
        count = 0;
        sum = 0;
        for(int j = 0; result[j] != '\0'; j++)
        {
            if(result[j] == 'O')
            {
                count++;
                sum += count;
            }
            else
            {
                count = 0;
            }
        }
        cout << sum << endl;
    }

    return 0;
}