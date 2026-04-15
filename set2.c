// SET-2
#include <stdio.h>
#include <string.h>

char input[100];
int i=0;

void S();
void L();

void S(){
    if(input[i]=='a') i++;
    else if(input[i]=='('){
        i++; L();
        if(input[i]==')') i++;
        else printf("Error\n");
    } else printf("Error\n");
}

void L(){
    S();
    while(input[i]==','){
        i++; S();
    }
}

int main(){
    scanf("%s",input);
    S();

    if(input[i]=='\0') printf("Accepted\n");
    else printf("Rejected\n");

    char str[100]; scanf("%s",str);
    int len=strlen(str);
    if(str[len-1]=='0') printf("Even\n");
    else printf("Odd\n");
}
