// Problem No.: 18270
// Solver:      Jinmin Goh
// Date:        20200718
// URL: https://www.acmicpc.net/problem/18270

#include <iostream>
#include <cstdlib>
#include <list>
#include <array>
#include <atomic>
#include <algorithm>
#include <deque>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <valarray>
#include <vector>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
using namespace std;

int main(){
    char names[8][10] = {"Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"};
    unordered_map < string, int > nameNumMap = {{"Beatrice", 0}, {"Belinda", 1}, {"Bella", 2}, {"Bessie", 3}, {"Betsy", 4}, {"Blue", 5}, {"Buttercup", 6}, {"Sue", 7}};
    bool visited[8] = {};
    int graph[8][2] = {};
    for(int i = 0; i < 8; i++){
        for(int j = 0; j < 2; j++){
            graph[i][j] = -1;
        }
    }
    // to find value with key, int temp = nameNumMap.find("Bessie") -> second;
    // it is same with int temp = nameNumMap.at("Bessie")
    int n;
    scanf("%d", &n);
    for(int _ = 0; _ < n; _++){
        char cow1[10], cow2[10];
        scanf("%s must be milked beside %s", cow1, cow2);
        int num1, num2;
        num1 = nameNumMap.at(cow1);
        num2 = nameNumMap.at(cow2);
        // printf("a %d %d\n", num1, num2);
        if(graph[num1][0] == -1){
            graph[num1][0] = num2;
        }
        else{
            graph[num1][1] = num2;
        }
        if(graph[num2][0] == -1){
            graph[num2][0] = num1;
        }
        else{
            graph[num2][1] = num1;
        }
    }

    
    for(int i = 0; i < 8; i++){
        // printf("%d %s\n", visited[i], names[i]);
        
        // pass visited node
        if(visited[i]){
            continue;
        }
        // no connection
        if(graph[i][0] == -1){
            printf("%s\n", names[i]);
            visited[i] = true;
        }
        // middle of connection
        else if(graph[i][1] != -1){
            continue;
        }
        // start of connection; meeds to fix
        else{
            printf("%s\n", names[i]);
            visited[i] = true;

            int curr = i, next = graph[i][0];
            int nextNext1 = graph[next][0], nextNext2 = graph[next][1];
            while(nextNext2 != -1){
                printf("%s\n", names[next]);
                visited[next] = true;
                if(curr == nextNext1){
                    curr = next;
                    next = nextNext2;
                    nextNext1 = graph[next][0];
                    nextNext2 = graph[next][1];
                }
                else{
                    curr = next;
                    next = nextNext1;
                    nextNext1 = graph[next][0];
                    nextNext2 = graph[next][1];
                }
            }
            printf("%s\n", names[next]);
            visited[next] = true;
        }
    }

    return 0;
}