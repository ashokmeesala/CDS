#include<stdio.h>
int max(int a,int b)
{
    return (a>b)? a : b;
}
void main()
{
    int a = 10;
    int b = 20;
    printf("max is %d ",max(a,b));
}