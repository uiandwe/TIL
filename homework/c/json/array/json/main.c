//
//  main.c
//  json
//
//  Created by Slogup on 2018. 2. 23..
//  Copyright © 2018년 Slogup. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include<string.h>

#define MAX_COLS 50

void getKey();
void getValue();
void getObj();
void insertVale(char *vlaue);

char str [MAX_COLS]= "";
int obj[10][2][2][MAX_COLS];

int pos = 0;
int j=0;
int size = 0;
int tab = 0;
int objIndex = 0;
int hashIndex = 0;
int duplicateHashIndex = 0;
char parentsName [MAX_COLS] = "";


void readFile(){
    FILE *pFile = NULL;
    
    pFile = fopen( "/Users/Slogup/Desktop/c.json", "r" );
    if( pFile != NULL )
    {
        char strTemp[255];
        char *pStr;
        
        while( !feof( pFile ) )
        {
            pStr = fgets( strTemp, sizeof(strTemp), pFile );
            //            printf( "%s", pStr );
            strcat(str, pStr);
        }
        fclose( pFile );
    }
    else
    {
        //에러 처리
    }

}

int hash(char *key){
    int hash = 0;
    for(int i=0; i<strlen(key); i++){
        int ascii = (int) key[i];
        hash+= ascii;
    }
    return hash % 10;
}


void getObj(){
    while (pos < size)       // 문서 크기만큼 반복
    {
        //        printf("%c %d \n", str[pos], pos);
        getKey();
        getValue();
        pos++;
    }
}


void getKey(){
    char name[MAX_COLS] = "";
    if(str[pos] == '\"' && pos < size){
        j = 0;
        pos++;
        while(str[pos] != '\"'){
            name[j] = str[pos];
            j++;
            pos++;
        }
        for(int k=0; k<tab; k++){
            printf("\t");
        }
        
        if(strlen(parentsName) > 0 && tab >= 1){
            char tempName[MAX_COLS] = "";
            strcat(tempName, parentsName);
            strcat(tempName, ".");
            strcat(tempName, name);
            strcpy(name, tempName);
        }
        printf("%s", name);
        
        hashIndex = hash(name);
        if(tab < 1){
            strcpy(parentsName, name);
        }
        
        
        for(int j=0; j<strlen(name); j++){
            obj[hashIndex][0][0][j] = name[j];
        }
        
    }
}

void getValue(){
    char jsonValue[MAX_COLS] = "";

    if(str[pos] == ':'){
        int j = 0;
        pos++;
        while(str[pos] != ',' && pos < size){
            
            if(str[pos] == '{'){
                tab++;
                printf("\n");
                getObj();
            }
            else{
                if(str[pos] == '}'){
                    pos++;
                    if(jsonValue[0] != ""){
                        parentsName[0] = '\0';
                        printf(" : %s \n", jsonValue);
                        insertVale(jsonValue);
                    }
                    tab--;
                    return ;
                }
                else{
                    jsonValue[j] = str[pos];
                    j++;
                }
                
            }
            pos++;
        }
        
        if(jsonValue != NULL && strlen(jsonValue) > 0){
            if(tab != 1){
                parentsName[0] = '\0';
            }
            
            printf(" : %s\n", jsonValue);
            insertVale(jsonValue);
        }
    }
}


void insertVale(char *value){
    for(int j=0; j<strlen(value); j++){
        obj[hashIndex][0][1][j] = value[j];
    }
}



int main(int argc, const char * argv[]) {
    // insert code here...
    
    readFile();

    size = strlen(str);
    
    
    if (str[pos] != '{')   // 문서의 시작이 {인지 검사
        return 0;
    
    pos++;    // 다음 문자로
    
    getObj(); //파싱 시작

    printf("-----------------------------------\n\n");
    
    
    for(int i=0; i<10; i++){
        for(int j=0; j<50; j++){
                printf("%c", obj[i][0][0][j]);
        }
        for(int j=0; j<50; j++){
            printf("%c", obj[i][0][1][j]);
        }

        
        printf("\n");
        
    }
    
    
    return 0;
}
