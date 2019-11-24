// Problem No.: 01008
// Solver:      Jinmin Goh
// Date:        191119
// URL: https://www.acmicpc.net/problem/1008

#include <stdio.h>

int main()
{
    int a, b;
    double c;
    scanf("%d %d", &a, &b);
    c = double(a)/b;
    printf("%.10lf", c);
    return 0;
}