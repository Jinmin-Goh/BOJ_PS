// Problem No.: 10869
// Solver:      Jinmin Goh
// Date:        191119
// URL: https://www.acmicpc.net/problem/10869

#include <stdio.h>

int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d\n%d\n%d\n%d\n%d", a+b, a-b, a*b, a/b, a%b);
    return 0;
}