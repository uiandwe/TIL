//
//  c15_1.c
//  test
//
//  Created by uiandwe on 2018. 2. 16..
//  Copyright © 2018년 uiandwe. All rights reserved.
//

#include "c15_1.h"

int arr[10];


void ShowArrayElem(int * param, int len){
    int i;
    
    for(i=0; i<len; i++) {
        printf("%d ", param[i]);
    }
    printf("\n");
}

void ShowOdd(){
    int i=0;
    for(;i<10; i++){
        if(arr[i]%2 != 0){
            printf("%d ", arr[i]);
        }
    }
    printf("\n");
}


void ShowEven(){
    int i=0;
    for(;i<10; i++){
        if(arr[i]%2 == 0){
            printf("%d ", arr[i]);
        }
    }
    printf("\n");
}

void input(){
    int i = 0;
    
    
    while(i < 10){
        int temp = 0;
        scanf("%d", &temp);
        arr[i] = temp;
        i++;
    }
}


void run15_1(){
    
    input();
    ShowArrayElem(arr, 10);
    ShowOdd();
    ShowEven();
    
}
