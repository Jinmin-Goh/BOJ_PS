// Problem No.: 10871
// Solver:      Jinmin Goh
// Date:        191121
// URL: https://www.acmicpc.net/problem/10871

#include <iostream>
#include <list>
using namespace std;

int main()
{
    // this code makes input & output fast as scanf / printf
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    // check following blog: https://starrykss.tistory.com/750
    
    int n, x;
    cin >> n >> x;
    
    int a[n];
    for(int i = 0; i < n; i++)
        cin >> a[i];

    list<int> ans;
    
    for(int i = 0; i < n; i++)
    {
        if(a[i] < x)
        {   
            ans.push_back(a[i]);
        }
    }
    
    int size = ans.size();
    for(int i = 0; i < size; i++)
    {
        cout << ans.front();
        ans.pop_front();
        if(i < size - 1)
            cout << " ";
    }

    return 0;
}