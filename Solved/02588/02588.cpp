// Problem No.: 02588
// Solver:      Jinmin Goh
// Date:        191119
// URL: https://www.acmicpc.net/problem/02588

#include <stdio.h>

int main()
{
    int a, b;
    scanf("%d\n%d", &a, &b);
    printf("%d\n%d\n%d\n%d", a*(b%10), a*((b/10)%10), a*(b/100), a*b);
    return 0;
}