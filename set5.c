// SET-5
#include <stdio.h>
#include <string.h>

int main(){
    char str[100];
    scanf("%s",str);

    if(strstr(str,"aaa")) printf("Accepted\n");
    else printf("Rejected\n");
}
