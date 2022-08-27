#include<stdio.h>
#include<stdlib.h>

char a1[] = "this will be present"; // this is comment
/* not present
in 
progWithCommentProcessed.c
file */char a2[] = "this will also be present";
int t1, /* comment removed*/ t2;
int main(){
    printf("Hello World");
    int knownLang = 12.0;
    if(knownLang >= 10){
        printf("You are pro");
        // another check
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