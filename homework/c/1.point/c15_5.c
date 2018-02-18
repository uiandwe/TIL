//
//  c15_5.c
//  test
//
//  Created by uiandwe on 2018. 2. 16..
//  Copyright © 2018년 uiandwe. All rights reserved.
//

#include "c15_5.h"

void sort(int *a)
{
    int i, j, t;
    
    for(i=0; i<6; i++)
    {
        for(j=0; j<6-i; j++)
        {
            if(a[j]<a[j+1])
            {
                t=a[j];
                a[j]=a[j+1];
                a[j+1]=t;
            }
        }
    }
    
    
}


void run15_5(){
    
    
    int i;
    int arr[7];
    
    printf("배열입력\n");
    for(i=0; i<7; i++)
    {
        scanf("%d", &arr[i]);
    }
    
    sort(arr);
    
    
    for(i=0; i<7; i++)
    {
        printf("%d ", arr[i]);
    }
    
    
    printf("\n");
    

    printf("\n end 15_5\n");
}
