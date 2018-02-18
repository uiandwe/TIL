//
//  quickSort.c
//  test
//
//  Created by uiandwe on 2018. 2. 16..
//  Copyright © 2018년 uiandwe. All rights reserved.
//

#include "quickSort.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


void quickSort(int *arr, int len, int fleft, int fright) {
    int left = fleft, right = fright;
    int pivot = arr[(fleft + fright) / 2];
    int i=0;
    
    do {
        while (arr[left] < pivot){
            left++;
        }
        
        while (arr[right] > pivot){
            right--;
        }
        
        if (left<= right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    } while (left<= right);
    
    /* recursion */
    if (fleft < right){
        quickSort(arr,  sizeof(arr)/sizeof(int), fleft, right);
    }
    
    if (left< fright){
        quickSort(arr,  sizeof(arr)/sizeof(int), left, fright);
    }
    
}




void runQuickSort(){
    int array[10];
    int i=0;
    
    srand(time(NULL));
    for(i=0; i<10; i++){
        array[i] = (rand() % 1000) +1;
    }
    
    for(i=0; i<10; i++){
        printf("%d ", array[i]);
    }
    printf("\n\n");
    
    quickSort(array, sizeof(array)/sizeof(int), 0, 9);
    
    for(i=0; i<10; i++){
        printf("%d ", array[i]);
    }
    printf("\n\n");
}
