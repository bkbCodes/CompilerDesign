#include<stdio.h>
#include<stdlib.h>

int main(){
    printf("Hello World");
    int knownLang = 12.0;
    if(knownLang >= 10){
        printf("You are pro");
    }
    else{
        if( knownLang < 5){
        printf("Fine");
        }
        else{
            printf("Beginner");
        }
    }
    return 0;
}