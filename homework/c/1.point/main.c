//
//  main.c
//  test
//
//  Created by uiandwe on 2018. 2. 11..
//  Copyright © 2018년 uiandwe. All rights reserved.
//

#include <stdio.h>
#include "c15_1.h"
#include "c15_2.h"
#include "c15_3.h"
#include "c15_4.h"
#include "c15_5.h"
#include "quickSort.h"
#include "hash.h"

void Swap3(int * num1, int * num2, int * num3){
    int temp = *num1;
    *num1 = *num2;
    *num2 = *num3;
    *num3 = temp;
}

int main(int argc, const char * argv[]) {
  

//    int arr[6] = {1, 2, 3, 4, 5, 6};
//    
//    
//    
//    ShowArrayElem(arr, sizeof(arr)/sizeof(int));
//    
//    int a = 1;
//    int b = 2;
//    int c = 3;
//    
//    Swap3(&a, &b, &c);
//    printf("%d, %d, %d", a, b, c);

    
//    run15_1();
//    run15_2();
//    run15_3();
//    run15_4();
//    run15_5();
    
//    runQuickSort();
    
    runHash();
    
    return 0;
}
