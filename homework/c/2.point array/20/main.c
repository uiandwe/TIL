//
//  main.c
//  20
//
//  Created by Slogup on 2018. 2. 25..
//  Copyright © 2018년 Slogup. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void turnArray(int (*arr)[4], int size){
    int i,j;
    int tempArray[size][size];
    int translatesArray[] = {3, 2, 1, 0};
    
    for(i=0; i<size; i++){
        for(j=0; j<size; j++){
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
    
    for(int k=0; k<4; k++){
        for(i=0; i<size; i++){
            int selectTranslateVal = translatesArray[i];
            for(j=0; j<size; j++){
                tempArray[j][selectTranslateVal] = arr[i][j];
            }
        
        }
    
        printf("\n\n");
    
        for(i=0; i<size; i++){
            for(j=0; j<size; j++){
                printf("%d ", tempArray[i][j]);
                arr[i][j] = tempArray[i][j];
            }
            printf("\n");
        }
    }
    
    
}


void q1(){
    
    int arr[4][4] = {
        
        { 1, 2, 3, 4 },
        
        { 5, 6, 7, 8 },
        
        { 9, 10, 11, 12 },
        
        { 13, 14, 15, 16 }
        
    };
    
    int arySize = sizeof(arr) / sizeof(arr[0]);
    
    
    turnArray(arr, arySize);

    
}


void makeSnail(int size){
    
    int matrix[10][10];
    int num=1;
    int curve=1;
    int limit=size;
    int i=0,j=-1;
    
    int p,q;
    
    while(1){
        
        //가로로 이동하면서 하나씩 할당
        for(p=0; p<limit; p++){
            j=j+curve;
            matrix[i][j]=num;
            num++;
        }
        
        //횟수 줄이고
        limit--;
        
        if(limit<0) break;
        
        //세로로 이동하면서 하나씩 할당
        for(p=0; p<limit; p++){
            i=i+curve;
            matrix[i][j]=num;
            num++;
        }
        
        curve=curve*-1;
    }
    
    //2차원 배열 출력
    for(p=0; p<size; p++){
        for(q=0; q<size; q++){
            printf("%d\t",matrix[p][q]);
        }
        printf("\n");
    }
    
    
}


int showArray(int (*ptrArr)[100], int size){
    
    int i,j;
    
    for(i=0; i<size; i++){
        
        for (j=0; j<size; j++)
            
            printf("%2d ", ptrArr[i][j]);
        
        printf("\n");
        
    }
    
    return 0;
    
}



void q2(){
    int num;
    
    int arr[100][100] = {0};
    
    printf("숫자를 입력하시오 : ");
    
    scanf("%d", &num);
    
    
    
    makeSnail(num);
    
}


void q3(){
    int i;
    
    for(i=0; i<5; i++)
        printf("난수 출력: %d \n", rand()%100);
    
}


void q4(){
    int dice1, dice2;
    
        
    srand((int)time(NULL));
        
    dice1 = rand()%6+1;
        
    srand((int)time(NULL)+dice1);
        
    dice2 = rand()%6+1;
        
        
        
    printf("주사위 1 : %d\n", dice1);
        
    printf("주사위 2 : %d\n", dice2);
    
}


int throwDice(int num, char *arr[], int *ptrWin, int *ptrDraw){
    
    int com_SRP;
    
    int lose = 0;
    
    srand((int)time(NULL)+num);
    
    com_SRP = rand()%3+1;
    
    
    
    printf("당신은 %s선택, 컴퓨터는 %s선택, ", arr[num], arr[com_SRP]);
    
    
    if(num-com_SRP==1||num-com_SRP==-2){
        
        printf("당신이 이겼습니다!\n");
        
        *ptrWin = *ptrWin + 1;
        
    } else if(num-com_SRP==0){
        
        printf("비겼습니다!\n");
        
        *ptrDraw = *ptrDraw + 1;
        
    } else if(num-com_SRP==2||num-com_SRP==-1){
        
        printf("당신이 졌습니다!\n");
        
        lose = 1;
        
    }
    
    return lose;
    
}



void q5(){
    int num;
    
    int win = 0, draw = 0, lose = 0;
    
    char *arr[4] = { "\0", "가위", "바위", "보"};
    
    
    
    while(lose == 0){
        
        printf("가위는 1, 바위는 2, 보는 3: ");
        
        scanf("%d", &num);
        
        if(1<=num&&num<=3){
            
            lose = throwDice(num, arr, &win, &draw);
            
        } else {
            
            printf("잘못된 입력입니다.\n");
            
        }
        
    }
    
    printf("\n게임의 결과 : %d승, %d무\n", win, draw);
    
}


int decide(int *user, int *com, int *result){
    
    int strikeCount = 0, ballCount = 0;
    
    int i,j;
    
    
    
    for(i=0; i<3; i++){
        
        for(j=0; j<3; j++){
            
            if(user[i] == com[j]){
                
                if(i == j){
                    
                    strikeCount++;
                    
                } else{
                    
                    ballCount++;
                    
                }
                
                
                
            }
            
        }
        
    }
    
    
    
    result[0] = strikeCount;
    
    result[1] = ballCount;
    
    
    
    if(strikeCount == 3)
        
        result[2] = 1;
    
    
    
    return 0;
    
}




void q6(){
    int count = 1,i;
    
    int userNum[3];
    
    int comNum[3] = { 22, 22, 22 };
    
    int result[3] = { 0, 0, 0 };    // result[0] - strike count, result[1] - ball count, result[2] - out count
    
    
    
    srand((int)time(NULL)+i);
    
    
    
    for(i=0; i<3;i++){
        
        comNum[i] = rand()%10;
        
        
        
        if( i == 1 && (comNum[0]==comNum[1])){
            
            i--;
            
        } else if ( i ==2 && ((comNum[0]==comNum[2]) || (comNum[1]==comNum[2])))
            
            i--;
        
    }
    
    
    
    for(i=0;i<3;i++){
        
        printf("컴퓨터의 선택 : %d ",comNum[i]);
        
    }
    
    printf("\n");
    
    
    
    printf("Start Game!\n");
    
    while (result[2] == 0){
        
        printf("3개의 숫자 선택: ");
        
        scanf("%d %d %d", &userNum[0], &userNum[1], &userNum[2]);
        
        
        
        if((0<=userNum[0] && userNum[0]<=9) &&
           
           (0<=userNum[1] && userNum[1]<=9) &&
           
           (0<=userNum[2] && userNum[2]<=9)) {
            
            decide(userNum, comNum, result);
            
            printf("%d번째 도전 결과: %dstrike, %dball!!\n", count, result[0], result[1]);
            
            count++;
            
            result[0] = 0, result[1] = 0;
            
        } else
            
            printf("잘못된 입력입니다.\n");
        
    }
    
    printf("Game Over!\n");
    
}



int main(int argc, const char * argv[]) {
    
//    q1();
//    q2();
//    q3();
//    q4();
//    q5();
    
    q6();
    
    return 0;
}
