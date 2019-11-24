// Problem No.: 10430
// Solver:      Jinmin Goh
// Date:        191119
// URL: https://www.acmicpc.net/problem/10430

#include <stdio.h>

int main()
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    printf("%d\n%d\n%d\n%d", (a+b)%c, (a%c + b%c)%c, (a*b)%c, (a%c * b%c)%c);
    return 0;
}