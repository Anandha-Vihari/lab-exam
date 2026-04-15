// SET-3
#include <stdio.h>
#include <string.h>

char input[100];
int i=0;

void E(); void Eprime(); void T(); void Tprime(); void F();

void E(){ T(); Eprime(); }

void Eprime(){
    if(input[i]=='+'){
        i++; T(); Eprime();
    }
}

void T(){ F(); Tprime(); }

void Tprime(){
    if(input[i]=='*'){
        i++; F(); Tprime();
    }
}

void F(){
    if(input[i]=='('){
        i++; E();
        if(input[i]==')') i++;
        else printf("Error\n");
    }
    else if(input[i]=='i' && input[i+1]=='d') i+=2;
    else printf("Error\n");
}

int main(){
    scanf("%s",input);
    E();

    if(input[i]=='\0') printf("Accepted\n");
    else printf("Rejected\n");

    char str[100]; scanf("%s",str);
    int len=strlen(str);

    if(len>=3 && str[len-3]=='a') printf("Accepted\n");
    else printf("Rejected\n");
}
