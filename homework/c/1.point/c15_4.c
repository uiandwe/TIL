//
//  c15_4.c
//  test
//
//  Created by uiandwe on 2018. 2. 16..
//  Copyright © 2018년 uiandwe. All rights reserved.
//

#include "c15_4.h"

void run15_4(){
    
    char str[100];
    int len = 0;
    int back = 0;
    _Bool bCheck = 1;
    
    scanf("%s", str);
    
    while(str[len]!='\0')
    {
        len++;
    }
    
    back = len-1;
    for(int i=0; i<len; i++){
        if(str[i] != str[back]){
            bCheck = 0;
            break;
        }
        back--;
    }
    
    
    if(bCheck == 1){
        printf("회문 ");
    }
    else{
        printf("회문 아님");
    }
    
    
    printf("\n end 15_4\n");
}
