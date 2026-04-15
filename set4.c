// SET-4
#include <stdio.h>
#include <string.h>

int main(){
    char str[100];
    scanf("%s",str);

    int len=strlen(str);

    if(len>=2 && str[len-1]=='0' && str[len-2]=='0')
        printf("Accepted\n");
    else
        printf("Rejected\n");

    if(str[len-1]=='1') printf("Odd\n");
    else printf("Even\n");
}
