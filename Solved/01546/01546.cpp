// Problem No.: 1546
// Solver:      Jinmin Goh
// Date:        20191128
// URL: https://www.acmicpc.net/problem/1546

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

    int n;
    cin >> n;
    int score[n], new_score[n], max = 0, sum = 0;
    for(int i = 0; i < n; i++)
    {
        cin >> score[i];
        if(max < score[i])
            max = score[i];
        sum += score[i];
    }
    double result = sum / (double)max * 100 / n;
    cout << result;
    

    return 0;
}