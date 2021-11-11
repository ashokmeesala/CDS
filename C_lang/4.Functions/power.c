#include<stdio.h>
int power(int base,int n)
{
    int pow = 1;
    for(int i=1;i<=n;i++)
        pow *=base;
    return pow;
}
void main()
{
    printf("%d",power(2,5));
}