// SET-1
#include <stdio.h>
#include <ctype.h>
#include <string.h>

char prod[10][10];
char result[20];
int n, idx=0;

void findFirst(char c){
    if(!isupper(c)){
        result[idx++]=c;
        return;
    }
    for(int i=0;i<n;i++){
        if(prod[i][0]==c){
            if(prod[i][2]=='$') result[idx++]='$';
            else findFirst(prod[i][2]);
        }
    }
}

int main(){
    scanf("%d",&n);
    for(int i=0;i<n;i++) scanf("%s",prod[i]);

    char symbol; scanf(" %c",&symbol);
    findFirst(symbol);

    printf("FIRST(%c) = { ",symbol);
    for(int i=0;i<idx;i++) printf("%c ",result[i]);
    printf("}\n");

    char str[100]; scanf("%s",str);
    int len=strlen(str);
    if(str[len-1]=='0') printf("Even\n");
    else printf("Odd\n");
}
