//
//  c15_2.c
//  test
//
//  Created by uiandwe on 2018. 2. 16..
//  Copyright © 2018년 uiandwe. All rights reserved.
//

#include "c15_2.h"

void run15_2(){
    
    int a = 0;
    int b[100];
    int i = 0;
    
    scanf("%d", &a);
    
    while(1){
        
        int x = a/2;
        int y = a%2;
        
        a = x;
        b[i] = y;
        if(a == 0){
            break;
        }
        i++;
    }
    
    
    for(int j=i; j>-1; j--){
        printf("%d", b[j]);
    }
    
    printf("\n end 15_2");
}
