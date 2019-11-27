// Problem No.: 4344
// Solver:      Jinmin Goh
// Date:        20191128
// URL: https://www.acmicpc.net/problem/4344

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

    int n, std_cnt;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> std_cnt;
        int score[std_cnt] = {}, score_sum = 0, high_std_cnt = 0;
        for(int j = 0; j < std_cnt; j++)
        {
            cin >> score[j];
            score_sum += score[j];
        }
        for(int j = 0; j < std_cnt; j++)
        {
            if(score[j] > score_sum / (double)std_cnt)
                high_std_cnt++;
        }
        cout << fixed;
        cout.precision(3);
        cout << high_std_cnt / (double)std_cnt * 100 << '%' << endl;
    }
    
    return 0;
}