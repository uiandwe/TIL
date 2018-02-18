//
//  c15_3.c
//  test
//
//  Created by uiandwe on 2018. 2. 16..
//  Copyright © 2018년 uiandwe. All rights reserved.
//

#include "c15_3.h"


void run15_3(){
    
    int array[10];
    int i=0;
    int input = 0;
    int front = 0;
    int back = 9;
    while(i < 10){
        scanf("%d", &input);
        if(input%2 == 0){
            array[back] = input;
            back--;
        }
        else{
            array[front] = input;
            front++;
        }
        
        i++;
    }
    
    for(i=0; i<10; i++){
        printf("%d ", array[i]);
    }
    printf("\n end 15_3");
}
