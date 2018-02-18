//
//  hash.c
//  test
//
//  Created by uiandwe on 2018. 2. 17..
//  Copyright © 2018년 uiandwe. All rights reserved.
//

#include "hash.h"


char hashtable[10][10];

int hash(char *key)
{
    int hash = 0;
    for(int i=0; i<strlen(key); i++){
        int ascii = (int) key[i];
        hash+= ascii;
    }
    return hash % 10;
    
}

void AddKey(char *key)
{
    int bucket;
    
    bucket = hash(key);
    printf("%s", key);
    for(int i=0; i<strlen(key); i++){
        hashtable[bucket][i] = key[i];
    }
    
}

int FindKey(char *key)
{
    
//    for(int i=0; i<10; i++){
//        
//        printf("%d %s\n", i, hashtable[i]);
//    }
    
    int bucket;
    
    bucket = hash(key);
    return (hashtable[bucket][0] == key[0]);
}

void runHash()
{
    int i, key;
    char s1[10];
  
  //  memset(hashtable, 0, sizeof(hashtable));
    for (i = 0; i < 5; i++)
    {
        printf("%d번째 값을 입력하세요 : ", i + 1);
        scanf("%s", s1);
        AddKey(s1);
    }
    
    printf("검색할 키를 입력하세요 : ");
    scanf("%s", s1);
    if (FindKey(s1))
    {
        puts("검색되었습니다.");
    }
    else
    {
        puts("입력하신 값은 없습니다..");
    }
}
