#include<stdio.h>
int strleng(char s[]);
void main()
{
    int len = strleng("ashok");
    printf("%d",len);
}
int strleng(char s[])
{
    int i = 0;
    while (s[i] != '\0')
        i++;
    return i;
}